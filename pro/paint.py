import jgraph
import matplotlib.pyplot as plt
import networkx as nx
import collections
import string
import random
from collections import defaultdict


def visualizeGraphCommunities(g, communities, algorithm):
    # Get the vertex count
    N = g.vcount()

    # Membership sequence(It refers to the community number to which a particular node belongs)

    member = communities.membership

    # Number of communities detected.
    print("Communities Detected by " + algorithm + ": ", max(member) + 1)

    # Mapping Colors to communities.
    color_map = jgraph.drawing.colors.ClusterColoringPalette(len(communities))

    # Make edge weight N*3 if the pair of nodes/vertex belongs to same community else make weight equal to 1
    eweights = {e.index: (N * 3)
                if member[e.tuple[0]] == member[e.tuple[1]]
                else 1
                for e in g.es}
    g.es["weight"] = [eweights[e.index] for e in g.es]

    # Vertex coloring based on communities.
    vcolors = {v: color_map[i]
               for i, c in enumerate(communities)
               for v in c}
    g.vs["color"] = [vcolors[v] for v in g.vs.indices]

    # Edge coloring based on communities.
    ecolors = {e.index: color_map[member[e.tuple[0]]]
               if member[e.tuple[0]] == member[e.tuple[1]]
               else "#e0e0e0"
               for e in g.es}
    g.es["color"] = [ecolors[e] for e in g.es.indices]

    # Calculating layout for graph plotting.
    l = g.layout_fruchterman_reingold(weights=g.es["weight"],
                                      maxiter=50,
                                      area=N ** 3,
                                      repulserad=N ** 3)

    # Plot the graph highlighting the detected communties.
    jgraph.plot(communities,
                'Result_FBData_' + algorithm + '.pdf',
                layout=l,
                vertex_size=2,
                edge_width=0.05,
                edge_curve=0.25,
                edge_arrow_size=0.1)


def load_graph(path):
    G = collections.defaultdict(dict)
    with open(path) as text:
        for line in text:
            vertices = line.strip().split()
            v_i = int(vertices[0])
            v_j = int(vertices[1])
            G[v_i][v_j] = 1.0
            G[v_j][v_i] = 1.0
    return G


def getCommunities_infomap(G):

    # Removing multiple edges, self-loops.
    G.simplify(multiple=True,
               loops=True,
               combine_edges=None)

    # Applying infomap algorithm to detect communities.
    communities = G.community_infomap(trials=100)

    # Return the communities object.
    return communities


class Vertex():

    def __init__(self, vid, cid, nodes, k_in=0):
        self._vid = vid
        self._cid = cid
        self._nodes = nodes
        self._kin = k_in  # 结点内部的边的权重


class Louvain():

    def __init__(self, G):
        self._G = G
        self._m = 0  # 边数量
        self._cid_vertices = {}  # 需维护的关于社区的信息(社区编号,其中包含的结点编号的集合)
        self._vid_vertex = {}  # 需维护的关于结点的信息(结点编号，相应的Vertex实例)
        for vid in list(self._G.keys()):
            self._cid_vertices[vid] = set([vid])
            self._vid_vertex[vid] = Vertex(vid, vid, set([vid]))
            self._m += sum([1 for neighbor in list(self._G[vid].keys())
                            if neighbor > vid])

    def first_stage(self):
        mod_inc = False  # 用于判断算法是否可终止
        visit_sequence = list(self._G.keys())
        random.shuffle(visit_sequence)
        while True:
            can_stop = True  # 第一阶段是否可终止
            for v_vid in visit_sequence:
                v_cid = self._vid_vertex[v_vid]._cid
                k_v = sum(self._G[v_vid].values()) + \
                    self._vid_vertex[v_vid]._kin
                cid_Q = {}
                for w_vid in list(self._G[v_vid].keys()):
                    w_cid = self._vid_vertex[w_vid]._cid
                    if w_cid in cid_Q:
                        continue
                    else:
                        tot = sum(
                            [sum(self._G[k].values()) + self._vid_vertex[k]._kin for k in self._cid_vertices[w_cid]])
                        if w_cid == v_cid:
                            tot -= k_v
                        k_v_in = sum(
                            [v for k, v in self._G[v_vid].items() if k in self._cid_vertices[w_cid]])
                        # 由于只需要知道delta_Q的正负，所以少乘了1/(2*self._m)
                        delta_Q = k_v_in - k_v * tot / self._m
                        cid_Q[w_cid] = delta_Q

                cid, max_delta_Q = sorted(
                    cid_Q.items(), key=lambda item: item[1], reverse=True)[0]
                if max_delta_Q > 0.0 and cid != v_cid:
                    self._vid_vertex[v_vid]._cid = cid
                    self._cid_vertices[cid].add(v_vid)
                    self._cid_vertices[v_cid].remove(v_vid)
                    can_stop = False
                    mod_inc = True
            if can_stop:
                break
        return mod_inc

    def second_stage(self):
        cid_vertices = {}
        vid_vertex = {}
        for cid, vertices in self._cid_vertices.items():
            if len(vertices) == 0:
                continue
            new_vertex = Vertex(cid, cid, set())
            for vid in vertices:
                new_vertex._nodes.update(self._vid_vertex[vid]._nodes)
                new_vertex._kin += self._vid_vertex[vid]._kin
                for k, v in self._G[vid].items():
                    if k in vertices:
                        new_vertex._kin += v / 2.0
            cid_vertices[cid] = set([cid])
            vid_vertex[cid] = new_vertex

        G = collections.defaultdict(dict)
        for cid1, vertices1 in self._cid_vertices.items():
            if len(vertices1) == 0:
                continue
            for cid2, vertices2 in self._cid_vertices.items():
                if cid2 <= cid1 or len(vertices2) == 0:
                    continue
                edge_weight = 0.0
                for vid in vertices1:
                    for k, v in self._G[vid].items():
                        if k in vertices2:
                            edge_weight += v
                if edge_weight != 0:
                    G[cid1][cid2] = edge_weight
                    G[cid2][cid1] = edge_weight

        self._cid_vertices = cid_vertices
        self._vid_vertex = vid_vertex
        self._G = G

    def get_communities(self):
        communities = []
        for vertices in self._cid_vertices.values():
            if len(vertices) != 0:
                c = set()
                for vid in vertices:
                    c.update(self._vid_vertex[vid]._nodes)
                communities.append(c)
        return communities

    def execute(self):
        iter_time = 1
        while True:
            iter_time += 1
            mod_inc = self.first_stage()
            if mod_inc:
                self.second_stage()
            else:
                break
        return self.get_communities()


if __name__ == '__main__':
    # G1 = load_graph(
    #     '/Users/shangjingwei/Documents/GitHub/python_lesson/pro/email.txt')

    # Read the Graph for community detection.
    G1 = jgraph.Graph.Read_Edgelist(
        '/Users/shangjingwei/Documents/GitHub/python_lesson/pro/email.txt', directed=False)
    print(type(G1))
    algorithm = Louvain(G1)
    communities = algorithm.execute()
    # communities_infomap = Louvain.get_communities(G2)
    print(communities)
    visualizeGraphCommunities(G1, communities, 'Louvain')
    for c in communities:
        print(c)

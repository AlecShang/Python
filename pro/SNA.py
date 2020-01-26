import igraph
import matplotlib.pyplot as plt
import networkx as nx


# Function to extract communities from the network using infomap algorithm
def getCommunities_infomap(G):

    # Removing multiple edges, self-loops.
    G.simplify(multiple=True,
               loops=True,
               combine_edges=None)

    # Applying infomap algorithm to detect communities.
    communities = G.community_infomap(trials=100)

    # Return the communities object.
    return communities

# Function to extract communities from the network using multilevel algorithm


def getCommunities_multilevel(G):

    # Removing multiple edges, self-loops.
    G.simplify(multiple=True,
               loops=True,
               combine_edges=None)

    # Applying multilevel algorithm to detect communities.
    communities = G.community_multilevel(return_levels=True)

    # Return the communities object.
    return communities

# Function to extract communities from the network using fastgreedy algorithm


def getCommunities_fastgreedy(G):

    # Removing multiple edges, self-loops.
    G.simplify(multiple=True,
               loops=True,
               combine_edges=None)

    # Applying fastgreedy algorithm to detect communities.
    communities = G.community_fastgreedy()

    # Plotting Dendograms
    print(str(communities.summary()))
    igraph.plot(communities, 'dendogram.pdf', orientation='bt')

    # Return the communities object.
    return communities.as_clustering()


def visualizeGraphCommunities(g, communities, algorithm):

    # Get the vertex count
    N = g.vcount()

    # Membership sequence(It refers to the community number to which a particular node belongs)

    member = communities.membership

    # Number of communities detected.
    print("Communities Detected by " + algorithm + ": ", max(member) + 1)

    # Mapping Colors to communities.
    color_map = igraph.drawing.colors.ClusterColoringPalette(len(communities))

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
    igraph.plot(communities,
                'Result_FBData_' + algorithm + '.pdf',
                layout=l,
                vertex_size=2,
                edge_width=0.05,
                edge_curve=0.25,
                edge_arrow_size=0.1)


# Read Graph from file for initial visualization.
g = nx.read_edgelist(
    '/Users/shangjingwei/Documents/GitHub/python_lesson/pro/email.txt')

# Graph info.
print(nx.info(g))

# Plot the initial network with k = 1
nx.draw(g, pos=nx.spring_layout(g, k=1),
        alpha=0.5,
        node_color='blue',
        node_size=1,
        width=0.05)

plt.show()

# Read the Graph for community detection.
G = igraph.Graph.Read_Edgelist(
    '/Users/shangjingwei/Documents/GitHub/python_lesson/pro/email.txt', directed=False)

print('Ground truth number of communities: 13477')

# Get communities and isualize graph communities..
communities_infomap = getCommunities_infomap(G)
visualizeGraphCommunities(G, communities_infomap, 'infomap')

communities_multilevel = getCommunities_multilevel(G)
visualizeGraphCommunities(G, communities_multilevel, 'multilevel')
for level, communities in enumerate(communities_multilevel):
    members = communities.membership
    print("Communities Detected by multilevel algorithm with level = "
          + str(level) + ": ", max(members) + 1)

communities_fastgreedy = getCommunities_fastgreedy(G)
visualizeGraphCommunities(G, communities_fastgreedy, 'fastgreedy')

print('Finish!')

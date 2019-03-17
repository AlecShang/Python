import sys

def Hanoverian_iteration(n,a,b,c):
    if n == 1:
        print(a, ' -> ', c)
        return None
    # 如果不是一个盘子的汉诺塔,则由A通过C转到B

    Hanoverian_iteration(n-1,a,c,b)
    print(a, ' -> ', c)
    #return(a, ' -> ', b)
    
    
    # 再由B通过A转到C
    # print(b, ' -> ', c)
    Hanoverian_iteration(n-1,b,a,c)
    
        #return(b, ' -> ', c)

print(Hanoverian_iteration(1, a = 'A', b = "B", c = 'C'))
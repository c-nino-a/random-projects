def dfs():
    print("{:^30s}".format("Graphs"))
    edges=int(input("Enter the required number of edges:"))
    vertices=int(input("Enter the required number of vertices:"))
    pairs=[]
    edgetable=[[0] * vertices for _ in range(vertices)]


    for edge in range(edges):
        x, y = input("Enter the format of the edges (format: x1 x2) : ").split()
        connections.append([x,y])

    for point in pairs:
        edgetable[point[0]-1][point[1]-1]=1

    for row in edgetable:
        for val in row:
            print(val,end=" "),
        print("")

    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    #     for row in edgetable]))

    start=int(input("Enter the source of the DFS: "))-1
    depth=int(input("Enter the depth-limit: "))
    visited=[]
    solve(start,edgetable,visited,depth)

def solve(current,edgetable,visited,depth):
    print(str(current+1),end="-> ")
    visited.append(current)
    if depth>0:
        while edgemap[current].count(1)!=0:
            try:    
                nextedge = edgemap[current].index(1)
                edgemap[current][nextedge] = 0
                if nextedge not in visited:
                    solve(nextedge,edgemap,visited,depth-1)
            except:
                pass

dfs()


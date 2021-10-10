def dfs():
    print("{:^30s}".format("Graphs"))
    edges=int(input("Enter the required number of edges:"))
    vertices=int(input("Enter the required number of vertices:"))
    
    connections=[]
    edgemap=[[0] * vertices for _ in range(vertices)]


    for edge in range(edges):
        con=list(map(int,input("Enter the format of the edges (format: x1 x2) : ").split()))
        connections.append(con)

    for point in connections:
        edgemap[point[0]-1][point[1]-1]=1

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in edgemap]))

    start=int(input("Enter the source of the DFS: "))-1
    target=int(input("Where to go?: "))-1
    visited=[]
    limit=int(input("Limit?: "))
    jack=solve(start,edgemap,visited,0,limit,target)
    print(jack)

def solve(current,edgemap,visited,level,limit,target):
    # print(str(current+1),end="-> ")
    visited.append(current)
    print(visited)
    # if current== target:
    #     return visited
    # indices = [i for i, x in enumerate(my_list) if x == "whatever"]
    while edgemap[current].count(1)!=0:
        print(str(current+1) + " has"+str(edgemap[current].count(1)))
        try:    
            nextedge = edgemap[current].index(1)
            
            if nextedge==target:
                return visited.append(target)
                break
            else:
                print(str(nextedge+1)+" is not target "+str(target+1))
                # print("from "+str(current+1) +" to "+str(nextedge+1))
                edgemap[current][nextedge] = 0
                if nextedge not in visited:
                    print(str(nextedge+1)+ " not visited")
                    if level+1 != limit:
                        print(str(level+1) + " is not limit")
                        print("going to "+str(nextedge+1))
                        solve(nextedge,edgemap,visited,level+1,limit,target)
                    else:
                        print(visited)
                        print("popping "+str(visited[-1]))
                        visited.pop(-1)
                print("Now at "+str(current+1))
        except:
            print("leaf")
            pass

dfs()
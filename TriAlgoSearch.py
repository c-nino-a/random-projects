class TriSearch:
    # def __init__(self):
    #     numedges=int(input("number of edges?"))
    #     numvert=int(input("number of vertices?"))
    #     connect=[]
    #     verts=input("Enter the names of the vertices (Space separated)").split()
    #     adjmatr=[[0] * numvert for _ in range(numvert)]

    #     for edge in range(numedges):
    #         ps,pe,w = input("Enter directed edge w/ weight").split()
    #         w = int(w)
    #         adjmatr[verts.index(ps)][verts.index(pe)]=w

    def __init__(self):
        numedges=10
        numvert=8
        connect=[]
        # verts=["S","A","F","C","B","D","E","G"]
        verts=["S","A","B","C","D","E","F","G"]
        heu=[6,4,5,2,2,8,4,0]
        adjmatr=[[0] * numvert for _ in range(numvert)]
        adjmatr[verts.index("S")][verts.index("A")]=2
        adjmatr[verts.index("S")][verts.index("F")]=3
        adjmatr[verts.index("S")][verts.index("B")]=1
        adjmatr[verts.index("B")][verts.index("D")]=2
        adjmatr[verts.index("B")][verts.index("E")]=4
        adjmatr[verts.index("A")][verts.index("C")]=2
        adjmatr[verts.index("A")][verts.index("D")]=3
        adjmatr[verts.index("F")][verts.index("G")]=6
        adjmatr[verts.index("C")][verts.index("G")]=4
        adjmatr[verts.index("D")][verts.index("G")]=4
        start="S"
        goal="G"
        print("Breadth-First Search:")
        self.bfs(start, goal, adjmatr,verts)
        print("")
        print("Depth-First Search:")
        self.dfs(start,goal,adjmatr,verts)
        print("")
        print("A-Star with Heuristic 6,4,5,2,2,8,4,0 for S,A,B,C,D,E,F,G respectively:")
        self.astar(start,goal,adjmatr,verts,heu)


    def bfs(self,start,goal,adjmatr,verts):
        queue=[]
        visited=[]
        queue.append(start)
        visited.append(start)
        while queue:
            start=queue.pop(0)
            print(start, end=" ")
            if start==goal:
                break   
            indices = [i for i, x in enumerate(adjmatr[verts.index(start)]) if x >0]
            for i in indices:
                if verts[i] not in visited:
                    queue.append(verts[i])
                    visited.append(verts[i])

    def dfs(self,start,g,adjmatr,verts): 
        visited = []
        stack = []
        stack.append(start)
        while (len(stack)):
            if start==g:
                break
            start = stack[-1]
            stack.pop()
            if start not in visited:
                print(start,end=' ')
                visited.append(start)
            C = [verts[adjmatr[verts.index(start)].index(vert)] for vert in adjmatr[verts.index(start)] if vert > 0]     #adjmatr[verts.index(start)][vert]
            for node in C:
                if (node not in visited):
                    stack.append(node)

    def astar(self,start,goal,adjmatr,verts,heu):
        # visited=[]
        # adist=[[0] * len(verts) for _ in range(len(verts))]
        # todist=[[0] * len(verts) for _ in range(len(verts))]
        # pnode=[[None] * len(verts) for _ in range(len(verts))]
        astardict={}
        for i in range(len(verts)):
            astardict[verts[i]]=[False,0,0,heu[i],""]
        
        # short=0
        # shortown=start
        queue=[start]
        # while (True):
        #     if start==goal:
        #         break
        while (len(queue)>0):
            # if astardict[start][1] !=0:
            #     prev=start
            # else:
            #     prev=0
            current=queue.pop(0)
            # start=shortown
            # short=0
            # shortown=""
            if not astardict[current][0]:
                # print(current, end=" ")
                astardict[current][0]=True
                C = [verts[adjmatr[verts.index(current)].index(vert)] for vert in adjmatr[verts.index(current)] if vert > 0]
                # pnode[verts.index(start)]=prev
                # astardict[start][4]=prev
                for neighbor in C:
                    # adist[verts.index(neighbor)] = adjmatr[verts.index(start)][verts.index(neighbor)]+adist[verts.index(pnode[verts.index(start))]]
                    # todist[verts.index(neighbor)]=adist[verts.index(neighbor)]+heu[verts.index(neighbor)]
                    
                    adistsub = adjmatr[verts.index(current)][verts.index(neighbor)] + astardict[current][1]
                    if astardict[neighbor][1]==0 or astardict[neighbor][1]>adistsub:
                        astardict[neighbor][1] = adistsub
                        astardict[neighbor][2] = astardict[neighbor][1]+astardict[neighbor][3]
                        astardict[neighbor][4] = current

            # for node in astardict:
            #     if short==0 and not astardict[node][0]:
            #         short=astardict[node][2]
            #         shortown=node
            #     if not astardict[node][0]:
            #         if astardict[node][2]<=short and astardict[node][2]>0:
            #             short=astardict[node][2]
            #             shortown=node

            queue=[x for x in sorted(astardict, key=lambda x: (astardict[x][2])) if not astardict[x][0] and astardict[x][2]>0 ]
            
            # visited.append(start)
        path=[goal]
        while path[0]!=start:
            path.insert(0,astardict[path[0]][4])
        for i in path:
            print(i, end=" ")







TriSearch()
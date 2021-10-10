import pygame
import sys
import time
  
pygame.init()
res = (800,400)
screen = pygame.display.set_mode(res)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,128,0)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial',30)

class lab1:
    def start(self,search):
        numedges=10
        numvert=8
        connect=[]
        self.visited=[]
        self.source=[]
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
        if search =="bfs":
            s=self.bfs(start, goal, adjmatr,verts)
        elif search =="dfs":
            s=self.dfs(start,goal,adjmatr,verts)
        elif search =="astar":
            s=self.astar(start,goal,adjmatr,verts,heu)
        visited=s

    def bfs(self,start,goal,adjmatr,verts):
        queue=[]
        visited=[]
        source=[]
        queue.append(start)
        visited.append(start)
        while queue:
            start=queue.pop(0)
            if start==goal:
                break   
            indices = [i for i, x in enumerate(adjmatr[verts.index(start)]) if x >0]
            for i in indices:
                if verts[i] not in visited:
                    queue.append(verts[i])
                    source+=len(verts[i])*start
                    visited.append(verts[i])
        self.visited=visited
        self.source=source



    def dfs(self,start,g,adjmatr,verts): 
        visited = []
        stack = []
        source=[]
        stack.append(start)
        while (len(stack)):
            if start==g:
                break
            start = stack[-1]
            stack.pop()
            source+=start
            if start not in visited:
                visited.append(start)
            C = [verts[adjmatr[verts.index(start)].index(vert)] for vert in adjmatr[verts.index(start)] if vert > 0]     #adjmatr[verts.index(start)][vert]
            for node in C:
                if (node not in visited):
                    stack.append(node)
        self.visited=visited
        self.source=source

    def astar(self,start,goal,adjmatr,verts,heu):
        astardict={}
        for i in range(len(verts)):
            astardict[verts[i]]=[False,0,0,heu[i],""]
        queue=[start]
        while (len(queue)>0):
            current=queue.pop(0)
            if not astardict[current][0]:
                astardict[current][0]=True
                C = [verts[adjmatr[verts.index(current)].index(vert)] for vert in adjmatr[verts.index(current)] if vert > 0]
                for neighbor in C:
                    adistsub = adjmatr[verts.index(current)][verts.index(neighbor)] + astardict[current][1]
                    if astardict[neighbor][1]==0 or astardict[neighbor][1]>adistsub:
                        astardict[neighbor][1] = adistsub
                        astardict[neighbor][2] = astardict[neighbor][1]+astardict[neighbor][3]
                        astardict[neighbor][4] = current

            queue=[x for x in sorted(astardict, key=lambda x: (astardict[x][2])) if not astardict[x][0] and astardict[x][2]>0]
        path=[goal]
        while path[0]!=start:
            path.insert(0,astardict[path[0]][4])
        source=path[:-1]
        self.visited=path
        self.source=source

    def draw (self,visited,screen,points,lines,source):
        place=50
        for i in visited:
            text2=smallfont.render(str(i), False, WHITE)
            screen.blit(text2,(150+place,height/2+140))
            print(i)
            if i != "S":
                try:
                    pygame.draw.line(screen,GREEN,points[int(ord(i)-64)],points[int(ord(source[visited.index(i)-1])-64)],3)           
                except:
                    pygame.draw.line(screen,GREEN,points[int(ord(i)-64)],points[0],3)
                pygame.draw.circle(screen,YELLOW,points[int(ord(i))-64],10)
            else:

                pygame.draw.circle(screen,YELLOW,points[0],10)
            pygame.display.update()
            time.sleep(.5)
            place+=30


    def __init__(self):
        active=False
        l=250
        w=135
        dispwid=800-60-120
        displeng=height/2-50-20
        xdist=160
        ydist=75
        rad=20
        points=[[l,w],[l+(xdist*1),w],[l+(xdist*1),w+(ydist)],
        [l+(xdist*2),w],[l+(xdist*2),w+(ydist)],[l+(xdist*2),w+(ydist*2)],
        [l+(xdist*2),w-(ydist)],[l+(xdist*3),w]]


        while True:
            
            for ev in pygame.event.get():
                
                if ev.type == pygame.QUIT:
                    pygame.quit()

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if 20 <= mouse[0] <= 20+150 and height/2-60 <= mouse[1] <= height/2-20:
                        self.start("bfs")
                        self.draw(self.visited,screen,points,lines,self.source)
                        active=True
                    elif 20 <= mouse[0] <= 20+150 and height/2 <= mouse[1] <= height/2+40:
                        self.start("dfs")
                        self.draw(self.visited,screen,points,lines,self.source)
                        active=True
                    elif 20 <= mouse[0] <= 20+150 and height/2+60 <= mouse[1] <= height/2+100:
                        self.start("astar")
                        self.draw(self.visited,screen,points,lines,self.source)
                        active=True

            screen.fill((0,0,128))

            mouse = pygame.mouse.get_pos()

            b1w=(800/2)-120-50
            b2w=(800/2)-50
            b3w=(800/2)+120-50
            if b1w <= mouse[0] <= b1w+100 and height/2 <= mouse[1] <= height/2+40:
                pygame.draw.rect(screen,YELLOW,[b1w,height/2,100,40])
            elif b2w <= mouse[0] <= b2w+100 and height/2 <= mouse[1] <= height/2+40:
                pygame.draw.rect(screen,YELLOW,[b2w,height/2,100,40])
            elif b3w <= mouse[0] <= b3w+100 and height/2 <= mouse[1] <= height/2+40:
                pygame.draw.rect(screen,YELLOW,[b3w,height/2,100,40])
            


            pygame.draw.rect(screen,GREEN,[20,height/2-60,150,40])
            pygame.draw.rect(screen,GREEN,[20,height/2,150,40])
            pygame.draw.rect(screen,GREEN,[20,height/2+60,150,40])
            bfs=smallfont.render("BFS", False, WHITE)
            screen.blit( bfs, (75,height/2-60))
            dfs=smallfont.render("DFS", False, WHITE)
            screen.blit( dfs, (75,height/2))
            astar=smallfont.render("A-Star", False, WHITE)
            screen.blit( astar, (75,height/2+60))
            

            display=pygame.draw.rect(screen,WHITE,[l/2+70,20,800-214,(height/2)+100])
            lines=[[points[0],points[1]],[points[0],points[6]],[points[0],points[2]],
            [points[1],points[3]],[points[3],points[7]],[points[2],points[4]],
            [points[2],points[5]],[points[1],points[4]],[points[6],points[7]],
            [points[4],points[7]]]
            for i in lines:
                pygame.draw.line(screen,BLACK,i[0],i[1],3)
            for i in points:
                pygame.draw.circle(screen,BLACK,i,rad)

            s=smallfont.render("S", False, WHITE)
            screen.blit(s,(points[0][0]-10,points[0][1]-15))
            a=smallfont.render("A", False, WHITE)
            screen.blit(a,(points[1][0]-10,points[1][1]-15))
            b=smallfont.render("B", False, WHITE)
            screen.blit(b,(points[2][0]-10,points[2][1]-15))
            c=smallfont.render("C", False, WHITE)
            screen.blit(c,(points[3][0]-10,points[3][1]-15))
            d=smallfont.render("D", False, WHITE)
            screen.blit(d,(points[4][0]-10,points[4][1]-15))
            e=smallfont.render("E", False, WHITE)
            screen.blit(e,(points[5][0]-10,points[5][1]-15))
            f=smallfont.render("F", False, WHITE)
            screen.blit(f,(points[6][0]-10,points[6][1]-15))
            g=smallfont.render("G", False, WHITE)
            screen.blit(g,(points[7][0]-10,points[7][1]-15))

            s2a=smallfont.render("2", False, RED)
            screen.blit(s2a,(l+(80*1),111))
            s2f=smallfont.render("3", False, RED)
            screen.blit(s2f,(l+(80*1),83))
            s2b=smallfont.render("1", False, RED)
            screen.blit(s2b,(l+(80*1),173))
            a2c=smallfont.render("2", False, RED)
            screen.blit(a2c,(l+(80*1),111))
            a2d=smallfont.render("3", False, RED)
            screen.blit(a2d,(l+(80*3),160))
            c2g=smallfont.render("4", False, RED)
            screen.blit(c2g,(l+(80*5),111))
            b2d=smallfont.render("2", False, RED)
            screen.blit(b2d,(l+(80*3),190))
            b2e=smallfont.render("4", False, RED)
            screen.blit(b2e,(l+(80*3),246))
            f2g=smallfont.render("6", False, RED)
            screen.blit(f2g,(l+(80*5),80))
            d2g=smallfont.render("4", False, RED)
            screen.blit(s2a,(l+(80*5),160))

            # heu=pygame.image.load("C:/Users/nino/Desktop/heu.png")
            # screen.blit(heu,(5,50))
            if not active:
                pygame.display.update()


lab1()
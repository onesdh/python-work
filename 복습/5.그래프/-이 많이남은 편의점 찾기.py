
class Graph() :
    def __init__(self, size) :
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g) :
    print(' ', end= ' ')
    for v in range(g.SIZE) :
        print("%9s" %storeAry[v][0], end = ' ')
    print()
    for row in range(g.SIZE) :
        print("%9s" %storeAry[row][0], end = ' ')
        for col in range(g.SIZE) :
            print("%8d" %g.graph[row][col], end = ' ')
        print()
    print()



G1 = None
storeAry = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4



gSize = 5
G1 = Graph(gSize)
G1.graph[GS25][CU] = 1; G1.graph[GS25][Seven11] = 1
G1.graph[CU][GS25] = 1; G1.graph[CU][Seven11] = 1; G1.graph[CU][MiniStop] = 1
G1.graph[Seven11][GS25] = 1; G1.graph[Seven11][CU] = 1; G1.graph[Seven11][MiniStop] = 1
G1.graph[MiniStop][Seven11] = 1; G1.graph[MiniStop][CU] = 1; G1.graph[MiniStop][Emart24] = 1
G1.graph[Emart24][MiniStop] = 1

print('## 편의점 그래프 ##')
printGraph(G1)

stack = []
visitedAry = []

current = 0
maxStore = current
maxCount = storeAry[current][1]
stack.append(current)
visitedAry.append(current)

while (len(stack) != 0) :
    next = None 
    for vertex in range(4) :
        if G1.graph[current][vertex] == 1 :
            if vertex in visitedAry :
                pass
            else :
                next = vertex
                break

    if next != None :
        current = next
        stack.append(current)   
        visitedAry.append(current)
        if storeAry[current][1] > maxCount :
            maxCount = storeAry[current][1]
            maxStore = current
    else :
        current = stack.pop()

print('허니버터침 최대 보유 쳔의점(개수) -->', storeAry[maxStore][0], '(', storeAry[maxStore][1], ')')
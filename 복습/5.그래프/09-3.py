#09-3 깊이 우선 탐색의 구현

class Graph() :
    def __init__(self, size) :
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = None
stack = []
visitedAry = []

G1 = Graph(4)
G1.graph[0][2] = 1
G1.graph[0][3] = 1

G1.graph[1][2] = 1

G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1

G1.graph[3][0] = 1
G1.graph[3][2] = 1

print("## G1 무방향 그래프##")
for row in range(4) :
    for col in range(4) :
        print(G1.graph[row][col], end = " ")
    print()

current = 0
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
    else :
        current = stack.pop()

print('방문순서 --> ', end = ' ')
for i in visitedAry :
    print(chr(ord('A')+i), end = ' ')

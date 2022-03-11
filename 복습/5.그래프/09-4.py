
gSize = 6

def findVertex(g, findVtx) :
    stack = []
    visitedAry = []

    current = 0
    stack.append(current)
    visitedAry.append(current)

    while (len(stack)!= 0) :
        next = None 
        for vertex in range(gSize) :
            if g.graph[current][vertex] != 0 :
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

    if findVtx in visitedAry :
        return True
    else :
        return False

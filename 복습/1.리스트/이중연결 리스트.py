class Node2() :
    def __init__ (self) :
        self.plink = None   #앞쪽 링크
        self.data = None
        self.nlink = None   #뒷쪽 링크

def printNodes(start) :
    current = start
    if current.nlink == None :
        return
    print("정방향 -->" , end = ' ')
    print(current.data, end = ' ')
    while current.nlink != None :
        current = current.nlink
        print(current.data, end = ' ')
    print()
    print("역방향 -->", end = ' ')
    print(current.data, end = ' ')
    while current.plink != None :
        current = current.plink
        print(current.data, end = ' ')


memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__" :

    node = Node2()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:] :
        pre = node
        node = Node2()
        node.data = data
        pre.nlink = node
        node.plink = pre
        memory.append(node)

    printNodes(head)

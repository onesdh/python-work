class Node2() :
    def __init__ (self) :
        self.plink = None   
        self.data = None
        self.nlink = None   

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

def insertNode(findData, insertData) :
    global memory, head, current, pre

    if head.data == findData:
        node = Node2()
        node.data = insertData
        node.nlink = head
        head.plink = node
        head = node
        return

    current = head
    while current.nlink != None :
        pre = current
        current = current.nlink
        if current.data == findData :
            node = Node2()
            node.data = insertData
            node.nlink = current
            current.plink = node
            pre.nlink = node
            node.plink = pre
            return

    node = Node2()
    node.data = insertData
    current.nlink = node 
    node.plink = current

def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData :
        current = head
        head = head.nlink
        head.plink = None
        del(current)
        return
    
    current = head
    while current.nlink != None :
        pre = current
        current = current.nlink
        if current.data == deleteData :
            if current.nlink == None :
                pre.nlink = current.nlink
                del(current)
                return
            pre.nlink = current.nlink
            next = current.nlink
            next.plink = pre
            del(current)
            return

def findNode(findData) :
    global memory, head, current, pre

    current = head
    if current.data == findData :
        return current
    while current.nlink != None :
        current = current.nlink
        if current.data == findData :
            return current
    return Node2()


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

    #insertNode("ㅁㅇ", "궁")

    #deleteNode("지효")
    #printNodes(head)

    #fnode = findNode("ㅁㅇㄴ")
    #print(fnode.data)

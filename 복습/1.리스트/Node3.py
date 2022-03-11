#원형리스트 odd홀수 even 짝수
import random

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    if current.link == None :
        return
    print(current.data, end = ' ')
    while current.link != start :
        current = current.link
        print(current.data, end = ' ')
    print()


def countOddEven():
    global memory, head, current, pre
    
    odd, even = 0, 0
    if head == None :
        return False
    current = head
    while True :
        if current.data %2 == 0 :
            even +=1
        else :
            odd += 1
        if current.link == head :
            break;
        current == current.link

    return odd, even

def makeZeronumber(odd, even) :
    if odd > even :
        reminder = 1
    else :
        reminder= 0

    current = head

    while True :
        if current.data % 2 == reminder :
            current.data *= -1
        if current.link == head :
            break;
        current = current.link




memory = []
head , current, pre = None, None, None

if __name__ == "__main__" :

    dataArray = []
    for _ in range(7) :
        dataArray.append(random.randint(1,100))

    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    oddCount, evenCount = countOddEven()
    print('홀수 -->', oddCount, '\t', '짝수 -->', evenCount)

    makeZeronumber(oddCount, evenCount)
    printNodes(head)

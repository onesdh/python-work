'''현재위치를 (0,0)이라 가정하고, 편의점 위치(x,y)와 거리가 가까운 순서대로 원형
연결 리스트를 생성하는 프로그램을 다음 조건에 맞게 작성한다

- 편의점 10개를 A, B, C, ... 순서로 이름을 부여한다
- 편의점 위치 x와 y는 1부터 100까지 랜덤하게 좌표가 생성되도록 한다.
- 현재위치와 편의점 거리는 (x^2 + y^2)의 제곱근(sqrt)으로 계산한다.
- 편의점 데이터 1개는 (편의점 이름, x좌표, y좌표) 형식의 튜플로 구성한다.'''

import random
import math

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printStores(start) :
    current = start
    if current == None :
        return

    while current.link != head :
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], '편의점, 거리:', math.sqrt(x*x + y*y))

    print()

def makeStoreList(store) :
    global memory, head, current, pre

    node = Node()
    node.data = store
    memory.append(node)

    if head == None :              #첫번째 편의점
        head = node
        node.link = head
        return
    #새 편의점이 첫번쨰 편의점보다 가까우면 첫편의점으로 만듦
    nodeX, nodeY = node.data[1:]
    nodeDist = math.sqrt(nodeX*nodeX + nodeY*nodeY)
    headX, headY = head.data[1:]
    headDist = math.sqrt(headX*headX + headY*headY)

    if headDist > nodeDist :       #헤드 앞에 삽입
        node.link = head
        last = head
        while last.link != head :
            last = last.link
        last.link = node
        head = node
        return
    
    current = head                #중간에 데이터를 넣을경우
    while current.link != head :
        pre = current
        current = current.link
        currX, currY = current.data[1:]
        currDist = math.sqrt(currX*currX + currY*currY)
        if currDist > nodeDist :
            pre.link = node
            node.link = current
            return
    current.link = node
    node.link = head

memory = []
head, current, pre = None, None, None

if __name__ == "__main__" :

    storeArray = []
    storeName = 'A'
    for _ in range(10) :
        store = (storeName, random.randint(1,100), random.randint(1,100))
        storeArray.append(store)
        storeName = chr(ord(storeName) + 1)

    for store in storeArray :
        makeStoreList(store)

    printStores(head)

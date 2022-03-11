
import random

class TreeNode() :
    def __init__(self) :
        self.left = None
        self.data = None
        self.right = None
        
memory = []
root = None
dataAry = ['바나나우유', '래쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sellAry = [random.choice(dataAry) for _ in range(20)]

print('오늘 판매된 물건(중복0) -->', sellAry)

node = TreeNode()
node.data = sellAry[0]
root = node
memory.append(node)

for name in sellAry[1:] :
    node = TreeNode()
    node.data = name
    
    current = root
    while True :
        if name == current.data :
            break
        if name < current.data :
            if current.left == None :
                current.left = node
                memory.append(node)
                break
            current = current.left
        else :
            if current.right == None :
                current.right = node
                memory.append(node)
                break
            current = current.right

print("이진탐색트리 구성 완료")
    
def preorder(node) :
    if node == None :
        return
    print(node.data, end = ' ')
    preorder(node.left)
    preorder(node.right)
    
print('오늘 판매된 물건(중복X) -->', end = ' ')
preorder(root)
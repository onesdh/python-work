class TreeNode() :
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None

memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] :

    node = TreeNode()
    node.data = name

    current = root
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else :
            if current.right == None :
                current.right = node
                break
            current = current.right

    memory.append(node)

findName = '마마무'

def searchitem(findName, root) :
    if findName == root.data :
        print(findName, '을(를) 찾음.')
        return root
    elif findName < root.data :
        searchitem(findName, root.left)
    else :
        searchitem(findName, root.right)
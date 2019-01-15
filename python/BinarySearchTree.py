class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def searchTree(root, key):
    if(root is None or root.val == key):
        return root
    elif(root.val < key):
        return searchTree(root.right, key)
    else:
        return searchTree(root.left, key)

def insertNode(root, node):
    if(root is None):
        root = node
    else:
        if(root.val < node.val):
            if(root.right is None):
                root.right = node
            else:
                insertNode(root.right, node)
        else:
            if(root.left is None):
                root.left = node
            else:
                insertNode(root.left, node)

nodeA = Node(5)
nodeB = Node(8)
nodeC = Node(11)
nodeD = Node(15)
nodeE = Node(4)

nodeA.left = nodeE
nodeA.right = nodeC
nodeC.left = nodeB
nodeC.right = nodeD

result = searchTree(nodeA, 11)
if result is not None:
    print(result.val)
else:
    print('Value not found in tree')

newNode = Node(17)
insertNode(nodeA, newNode)
print(nodeD.right.val)
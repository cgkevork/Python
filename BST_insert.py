class Node:
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None
		

def binary_insert(root,node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                binary_insert(root.left,node)
        else:
            if root.right is None:
                root.right = node
            else:
                binary_insert(root.right,node)
                
def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print root.data
    in_order_print(root.right)
    
def pre_order_print(root):
    if not root:
        return
    print root.data
    pre_order_print(root.left)
    pre_order_print(root.right)
    
r = Node(3)

binary_insert(r, Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(5))


print "in order:"
in_order_print(r)

print "pre order"
pre_order_print(r)
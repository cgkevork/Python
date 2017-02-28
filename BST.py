A = [2, 4, 5, 7, 13, 14, 15, 23]

def BST(A, n, x):
    low = 0
    high = n-1
    
    while (low <= high):
        mid = (low + high)/2
        
        if (x == A[mid]):
            return mid  #answer found
        elif (x < A[mid]):
            high = mid -1  # x lies before mid
        else:  
            low == mid + 1  # x lies after mid
            
x = input("please input a value to search: ")
ans = BST(A, len(A), x)
print(str(x)  + " lies at position " + str(ans))


class Tree(object):
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right
        
    def insert(item, tree):
        if (item < tree.entry):
            if (tree.left != None):
                insert(item, tree.left)
            else:
                tree.left = Tree(item)
        else:
            if (tree.right != None):
                insert(item, tree.right)
            else:
                tree.right = Tree(item)
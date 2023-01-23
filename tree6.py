class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None


def is_btree(node):
    test1=False
    test2=False
    if node:
       if node.left:
          test1=True if node.left.value<node.value else False
       else:
          test1=True

       if node.right:
          test2=True if node.right.value>node.value else False
       else:
          test2=True

       return test1 and test2 and is_btree(node.left) and is_btree(node.right)
    else:
       return True

if __name__=="__main__":
   print("=============================")
   print("The binary tree is bst r not:")
   node=Node(12)
   node.right=Node(16)
   node.left=Node(8)
   node.right.right=Node(20)
   node.right.left=Node(14)
   node.left.right=Node(10)
   node.left.left=Node(6)
   print(is_btree(node))
   print("===============================")
   print("Checking if its btree:")
   node=Node(10)
   node.right=Node(100)
   node.left=Node(80)
   node.right.right=Node(20)
   node.right.left=Node(14)
   node.left.right=Node(10)
   node.left.left=Node(6)
   print(is_btree(node))
   print("=================================")

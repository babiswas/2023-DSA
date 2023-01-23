class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def flip(node1,node2):
    if not node1 and not node2:
       return not node1 and not node2
    if node1.value!=node2.value:
       return False
    a=flip(node1.left,node2.left) and flip(node1.right,node2.right)
    return a or flip(node.left,node.right) or flip(node.right,node.left)

if __name__=="__main__":
   print("============================")
   print("Constructing tree1:")
   node=Node(1)
   node.left=Node(2)
   node.right=Node(3)
   node.left.right=Node(5)
   node.left.left=Node(4)
   node.left.right.left=Node(7)
   node.left.right.right=Node(8)
   node.right.left=Node(6)
   print("=============================")
   print("Constructing tree2:")
   node1=Node(1)
   node1.left=Node(3)
   node1.right=Node(2)
   node1.left.right=Node(6)
   node1.right.left=Node(4)
   node1.right.right=Node(5)
   node1.right.right.left=Node(8)
   node1.right.right.right=Node(7)
   print("===================================")
   print("Can be flipped:")
   test=flip(node,node1)
   print(test)
   print("================================")
   
   
class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def inorder(node,K):
    stack=list()
    temp=node
    while True:
       if K==0:
          print(val)
          break
       if temp:
          stack.append(temp)
          temp=temp.left
       elif stack:
          temp=stack.pop()
          val=temp.value
          K-=1
          temp=temp.right
       else:
          break

if __name__=="__main__":
   print("========================")
   print("The bst tree is")
   node=Node(12)
   node.right=Node(16)
   node.right.right=Node(20)
   node.right.left=Node(14)
   node.left=Node(8)
   node.left.right=Node(10)
   node.left.left=Node(6)
   print("======================")
   print("The inorder traversal of the tree is:")
   inorder(node,3)
   print("==============================")

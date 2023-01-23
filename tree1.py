class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def inorder(self):
       if self:
          if self.left:
             self.left.inorder()
          print(self.value)
          if self.right:
             self.right.inorder()

   def is_balanced(self):
       lh=0
       rh=0
       if not self:
          return 0
       if self.left:
          lh=self.left.is_balanced()
       if self.right:
          rh=self.right.is_balanced()
       if lh==-1 or rh==-1:
          return -1
       if abs(lh-rh)>1:
          return -1
       return 1+max(lh,rh)

   def insert(self,value):
       if self.value>value:
          if self.left:
             self.left.insert(value)
          else:
             self.left=Node(value)
       elif self.value<value:
          if self.right:
             self.right.insert(value)
          else:
             self.right=Node(value)
       else:
          print("Duplication not allowed:")

if __name__=="__main__":
   print("========================")
   print("Check if the tree is balanced:")
   node=Node(12)
   node.insert(16)
   node.insert(8)
   node.insert(14)
   node.insert(20)
   node.insert(6)
   node.insert(10)
   node.insert(22)
   node.insert(23)
   node.insert(24)
   node.insert(25)
   print("The inorder traversal of the tree is:")
   node.inorder()
   print("=============================")
   height=node.is_balanced()
   if height!=-1:
      print("The tree is balanced:")
   else:
      print("The tree is not balanced:")
   print(f"The height of the tree is {height}")
   print("===============================")
   
   
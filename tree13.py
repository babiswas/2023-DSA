class Node:
   maxi=0
   def __init__(self,value):
         self.value=value
         self.left=None
         self.right=None

   def inorder(self):
         stack=list()
         temp=self
         while True:
            if temp:
               stack.append(temp)
               temp=temp.left
            elif stack:
               temp=stack.pop()
               print(temp.value)
               temp=temp.right
            else:
               break

   def maxm(self):
         lh=0
         rh=0
         if not self:
            return 0
         if self.left:
            lh=self.left.maxm()
         if self.right:
            rh=self.right.maxm()
         Node.maxi=max(Node.maxi,self.value+lh+rh)
         return self.value+max(lh,rh)
         
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
   print("==========================")
   print("Constructing the tree:")
   node=Node(12)
   node.insert(16)
   node.insert(14)
   node.insert(20)
   node.insert(8)
   node.insert(10)
   node.insert(6)
   print("======================")
   print("Inorder traversal of the tree:")
   node.inorder()
   print("======================")
   print("The maximum sum tree is:")
   m=node.maxm()
   if m>Node.maxi:
      print(f"The maximum sum tree is {m}")
   else:
      print(f"the maximum sum tree is {Node.maxi}")
   print("===========================")
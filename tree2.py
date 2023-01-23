class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def postorder(self):
       stack=list()
       temp=self
       count=0
       while True:
           if temp:
              stack.append(temp)
              temp=temp.left
           else:
              if not stack:
                 break
              if stack[-1].right==None:
                 maxm=max([node.value for node in stack])
                 if maxm==stack[-1].value:
                    count+=1
                 temp=stack.pop()
                 while stack[-1].right==temp:
                      maxm=max([node.value for node in stack])
                      if maxm==stack[-1].value:
                         count+=1
                      temp=stack.pop()
                      if not stack:
                         break
              if stack:
                 temp=stack[-1].right
              else:
                 break
       return count
                 
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
   print("==============================")
   print("Constructing the tree:")
   node=Node(12)
   node.insert(16)
   node.insert(20)
   node.insert(14)
   node.insert(8)
   node.insert(10)
   node.insert(6)
   print("=================================")
   print("Count good nodes in a tree:")
   count=node.postorder()
   print("The good nodes in a tree is:",count)
   print("=============================")

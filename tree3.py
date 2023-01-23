class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

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

   def count_good_nodes(self,maxm):
       if not self:
          return 0
       res=1 if self.value>maxm else 0
       if self.value>maxm:
          print(self.value)
          maxm=self.value
       if self.left:
          res+=self.left.count_good_nodes(maxm)
       if self.right:
          res+=self.right.count_good_nodes(maxm)
       return res

if __name__=="__main__":
   print("===========================")
   node=Node(12)
   node.insert(8)
   node.insert(16)
   node.insert(20)
   node.insert(14)
   node.insert(10)
   node.insert(6)
   count=node.count_good_nodes(0)
   print(f"The number of good nodes is {count}")
   print("============================")
class Node:
   test=''
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def serialize(self):
       if not self:
          Node.test+=",N"
       if Node.test=="":
          Node.test+=str(self.value)
       else:
          Node.test+=","+str(self.value)
       if self.left:
          self.left.serialize()
       else:
          Node.test+=",N"
       if self.right:
          self.right.serialize()
       else:
          Node.test+=",N"

if __name__=="__main__":
   print("======================")
   print("Constructing tree:")
   node=Node(12)
   node.left=Node(8)
   node.right=Node(16)
   node.left.right=Node(10)
   node.left.left=Node(6)
   node.right.right=Node(20)
   node.right.left=Node(14)
   print("=======================")
   print("Serializing binary tree:")
   node.serialize()
   print(Node.test)
   print("==========================")
   
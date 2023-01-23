class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def lvl(node):
   queue=list()
   queue.append(node)
   while queue:
      q_len=len(queue)
      print([nd.value for nd in queue])
      while q_len:
         m=queue.pop(0)
         if m.left:
            queue.append(m.left)
         if m.right:
            queue.append(m.right)
         q_len-=1

def merge(node1,node2):
    if node1 and node2:
       node1.value=node1.value+node2.value
       node1.left=merge(node1.left,node2.left)
       node1.right=merge(node1.right,node2.right)
       return node1
    elif node1 and not node2:
       node1.value=node1.value
       node1.left=merge(node1.left,None)
       node1.right=merge(node1.right,None)
       return node1
    elif not node1 and node2:
       node1.value=node2.value
       node1.left=merge(None,node2.left)
       node1.right=merge(None,node2.right)
       return node1
    elif not node1 and not node2:
       return None 

if __name__=="__main__":
   print("========================")
   print("Level order traversal of the node is:")
   node1=Node(2)
   node1.right=Node(3)
   node1.left=Node(1)
   node1.right.right=Node(5)
   node1.right.left=Node(1)
   node1.left.right=Node(10)
   node1.left.left=Node(6)
   lvl(node1)
   print("===========================")
   print("Level order traversal of the node is:")
   node2=Node(2)
   node2.right=Node(3)
   node2.left=Node(1)
   node2.right.right=Node(5)
   node2.right.left=Node(1)
   node2.left.right=Node(10)
   node2.left.left=Node(6)
   lvl(node2)
   print("==============================")
   print("Merging two trees:")
   node1=merge(node1,node2)
   lvl(node1)
   print("===============================")
   
   
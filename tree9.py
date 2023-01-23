class Node:
  def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

def invert_tree(node):
    if node:
       node.left,node.right=node.right,node.left
       node.left=invert_tree(node.left)
       node.right=invert_tree(node.right)
       return node

def lvl(node):
    queue=list()
    queue.append(node)
    while queue:
        q_len=len(queue)
        print([m.value for m in queue])
        while q_len:
           m=queue.pop(0)
           if m.left:
              queue.append(m.left)
           if m.right:
              queue.append(m.right)
           q_len-=1

if __name__=="__main__":
   node=Node(12)
   node.right=Node(16)
   node.right.right=Node(20)
   node.right.left=Node(14)
   node.left=Node(8)
   node.left.right=Node(10)
   node.left.left=Node(6)
   print("=======================")
   print("Level order traversal of the tree is:")
   lvl(node)
   print("=========================")
   print("Inverting the tree is:")
   node=invert_tree(node)
   lvl(node)
   print("=========================")
class Node:
  def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

def construct_btree(arr,left,right):
    if left<=right:
       mid=(left+right)//2
       node=Node(arr[mid])
       node.left=construct_btree(arr,left,mid-1)
       node.right=construct_btree(arr,mid+1,right)
       return node
    else:
       return None

def lvl(node):
   queue=list()
   queue.append(node)
   while queue:
       ql=len(queue)
       print([m.value for m in queue])
       while ql:
         m=queue.pop(0)
         if m.left:
            queue.append(m.left)
         if m.right:
            queue.append(m.right)
         ql-=1

if __name__=="__main__":
   print("======================")
   print("Constructing tree from sorted array:")
   arr=[1,2,3,4,5,6,7,8]
   node=construct_btree(arr,0,7)
   print("Level order traversal of the tree:")
   lvl(node)
   print("=====================")
   
   
   
         
       
    
   
from heapq import heapify
from heapq import heappush
from heapq import heappushpop
from heapq import nlargest

class Maxheap:
   def __init__(self,num):
       self.h=list()
       self.length=num
       heapify(self.h)

   def add(self,element):
       if len(self.h)<self.length:
           heappush(self.h,element)
       else:
           heappushpop(self.h,element)

   def get_top(self):
      return nlargest(self.length,self.h)

if __name__=="__main__":
   print("====================================")
   mp=Maxheap(6)
   for i in range(106):
     mp.add(i)
   l=mp.get_top()
   print(l)
   print(l[-1])
   print("====================================")


from heapq import heapify
from heapq import heappushpop
from heapq import nlargest
from heapq import heappush

class Myheap:
   def __init__(self,num):
       self.h=list()
       self.length=num
       heapify(self.h)

   def top(self):
      return nlargest(self.length,self.h)
      
   def add(self,element):
       if len(self.h)<self.length:
          heappush(self.h,element)
       else:
          heappushpop(self.h,element)

def all_possible_sum(arr):
    sum=0
    temp=list()
    for i in range(len(arr)):
       sum+=arr[i]
       temp.append(sum)
       if i+1<len(arr):
          for j in range(i+1,len(arr)):
             sum+=arr[j]
             temp.append(sum)
       else:
         break
    return temp

def kth_sum_subarray(arr,K):
    temp=all_possible_sum(arr)
    hp=Myheap(K)
    for i in temp:
       hp.add(i)
    return hp.top()

if __name__=="__main__":
   print("========================")
   print("The kth sum subarray is:")
   arr=[10, -10, 20, -40]
   num=kth_sum_subarray(arr,6)
   print(num)
   print("==========================")

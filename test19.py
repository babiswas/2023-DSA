import sys
def all3subarray(arr,count):
   index1=0
   index2=0
   sum=0
   mylist=list()
   while index1<len(arr) and index2<len(arr) and index1<=index2:
       sum+=arr[index2]
       if index2-index1+1==count:
          mylist.append(sum)
          sum-=arr[index1]
          index1+=1
       index2+=1
   return mylist

def allsubarray(arr,count):
   index1=0
   index2=0
   sum=0
   maxm=-sys.maxsize+1
   while index1<len(arr) and index2<len(arr) and index1<=index2:
       sum+=arr[index2]
       if index2-index1+1==count:
          if maxm<sum:
             maxm=sum
          sum-=arr[index1]
          index1+=1
       index2+=1
   return maxm

if __name__=="__main__":
   print("=======================")
   arr=[1,2,3,4,5,6]
   print("All subarrays of length 3 is:")
   l=all3subarray(arr,3)
   print(l)
   print("========================")
   print("The maximum sum subarray of length 3")
   print(max(l))
   print("=========================")
   num=allsubarray(arr,3)
   print(f"The maximum sum is {num}")
   print("=========================")
   
         

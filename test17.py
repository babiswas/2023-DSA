def equilibrium(arr):
   current_sum=0
   sm=sum(arr)
   index1=0
   while index1<len(arr):
       temp=sm-arr[index1]-current_sum
       if temp==current_sum:
          return index1
       current_sum+=arr[index1]
       index1+=1
   return -1

def equilibrium2(arr):
   for i in range(1,len(arr)):
      arr[i]=arr[i]+arr[i-1]
   for i in range(len(arr)):
     if arr[len(arr)-1]-arr[i]==arr[i-1]:
        return i
   return -1

if __name__=="__main__":
   print("=======================")
   print("The equilibrium index in the array is:")
   arr=[-7,1,5,2,-4,3,0]
   index=equilibrium(arr)
   print(index)
   print("========================")
   print("Second version of the equilibrium:")
   index=equilibrium2(arr)
   print(index)
   print("==========================")
   
   
       
       
       
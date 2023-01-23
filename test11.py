def k_operations(arr,K):
   maxm=max(arr)
   result=0
   for i in range(len(arr)):
      if (maxm-arr[i])%K!=0:
         return -1
      result+=(maxm-arr[i])//K
   return result

if __name__=="__main__":
   print("========================")
   print("Minimum number of operations of increment by k is:")
   arr=[4,7,19,16]
   ops=k_operations(arr,3)
   print(f"the minimum number of operations is {ops}")
   print("=====================================")
   print("Minimum number of operations of increment by k is:")
   arr=[4,4,4,4]
   ops=k_operations(arr,3)
   print(f"the minimum number of operations is {ops}")
   print("=======================================")
   
      
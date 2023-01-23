def majority_element(arr):
   count=1
   test=arr[0]
   for i in range(1,len(arr)):
      if arr[i]==test:
         count+=1
      else:
         count-=1
      if count<0:
         test=arr[i]
   count=0
   for i in range(len(arr)):
      if arr[i]==test:
         count+=1
   print(f"The majority element is {test} and count is {count}")
   return count

if __name__=="__main__":
   print("=========================")
   print("Finding the majority element")
   arr=[3,3,4,2,4,4,2,4,4]
   majority_element(arr)
   brr=[5,1,4,1,1]
   majority_element(brr)
   print("===========================")
   




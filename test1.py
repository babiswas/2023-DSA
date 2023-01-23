def rearrange(arr):
   mp=dict()
   for i in arr:
     if i!=-1:
        mp.update({i:True})
   for i in range(len(arr)):
      index=mp.get(i,False)
      if index:
         arr[i]=i
      else:
         arr[i]=-1

def rearrange_2(arr):
   for i in range(len(arr)):
      if arr[i]>0 and arr[i]!=i:
         arr[arr[i]],arr[i]=arr[i],arr[arr[i]]


if __name__=="__main__":
   print("==========================")
   print("Rearranging the array:")
   arr=[-1,-1,6,1,9,3,2,-1,4,-1]
   rearrange(arr)
   print(arr)
   print("===========================")
   print("Second implementation:")
   arr=[-1,-1,6,1,9,3,2,-1,4,-1]
   rearrange_2(arr)
   print(arr)
   print("==============================")
   
   
   
   
      
      
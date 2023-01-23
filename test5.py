def rotations(arr):
   l,r=0,len(arr)-1
   res=arr[0]
   index=0
   while l<r:
      if arr[l]<arr[r]:
         res=min(arr[l],res)
         if res==arr[l]:
            index=l
         break
      mid=(l+r)//2
      res=min(res,arr[mid])
      if res==arr[mid]:
         index=mid
      if arr[mid]>arr[l]:
         l=mid+1
      else:
         r=mid
   print(res)
   return index

if __name__=="__main__":
   print("===========================")
   arr=[5,6,7,8,9,10,1,2,3,4]
   print("The number of raotation in the array is:")
   index=rotations(arr)
   print(index)
   print("=============================")
         
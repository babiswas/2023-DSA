def search(arr,target):
   l,r=0,len(arr)-1
   while l<=r:
      mid=(l+r)//2
      if arr[mid]==target:
         return mid
      if arr[mid]>arr[l]:
         if target>arr[mid] or target<arr[l]:
            l=mid+1
         else:
            r=mid-1
      else:
         if target>arr[mid] or target<arr[r]:
            l=mid+1
         else:
            r=mid-1
   return -1


if __name__=="__main__":
   print("===============================")
   print("Search in rotated array:")
   arr=[4,5,6,1,2,3]
   for i in arr:
      index=search(arr,i)
      print(index)
   print("===============================")
   
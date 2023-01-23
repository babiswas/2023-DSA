def find_missingnum(arr,m):
    if arr[0]!=0:
       return 0
    if arr[-1]!=m-1:
       return m-1
    for i in range(1,len(arr)):
      if arr[i-1]+1!=arr[i]:
         return i

if __name__=="__main__":
   print("===================")
   arr=[0,1,2,6,9]
   index=find_missingnum(arr,10)
   print(index)
   print("======================")
   arr=[4,5,10,11]
   index=find_missingnum(arr,12)
   print(index)
   print("=====================")
   arr=[0,1,2,3]
   index=find_missingnum(arr,5)
   print(index)
   print("======================")
   arr=[0,1,2,3,4,5,6,7,10]
   index=find_missingnum(arr,11)
   print(index)
   print("========================")
   arr=[0,1,2,3]
   index=find_missingnum(arr,5)
   print(index)
   print("========================")
   
def sort_0s_1s(arr):
   index=-1
   for i in range(len(arr)):
       if arr[i]==0:
          index+=1
          arr[index],arr[i]=arr[i],arr[index]
   for i in range(index+1,len(arr)):
       if arr[i]==1:
          index+=1
          arr[index],arr[i]=arr[i],arr[index]
   return arr

if __name__=="__main__":
   print("==========================")
   print("Sorting 0 1 and 2")
   arr=[0,1,2,0,1,2]
   sort_0s_1s(arr)
   print(arr)
   print("===========================")
   
   
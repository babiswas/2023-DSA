def find_max_subarr(arr,k):
    queue=list()
    index1=0
    index2=0
    while index1<len(arr) and index2<len(arr) and index1<=index2:
          if not queue:
             queue.append(arr[index2])
          else:
             if queue[0]<arr[index2]:
                queue.insert(0,arr[index2])
             elif queue[0]>=arr[index2]:
                queue.append(arr[index2])
          if index2-index1+1==k:
             print(arr[index1:index2+1])
             num=queue[0]
             print(num)
             if arr[index1]==num:
                queue.pop(0)
             index1+=1
          index2+=1

if __name__=="__main__":
   print("==================================")
   print("The maximum in subarray of length K is:")
   arr=[1,2,3,1,4,5,2,3,6]
   find_max_subarr(arr,3)
   print("==================================")
   print("The maximum in the subarray is:")
   brr=[4,1,3,2,6]
   find_max_subarr(brr,3)
   print("==================================")
   
   
             
              
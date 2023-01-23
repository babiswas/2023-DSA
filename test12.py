import sys
def smallest_subarray(arr,val1):
    index1=0
    index2=0
    count=0
    val2=0
    maxm=sys.maxsize-1
    while index1<=index2 and index1<len(arr) and index2<len(arr):
        val2+=arr[index2]
        if val2>val1:
           count=index2-index1+1
           print(count)
           if count<maxm:
              maxm=count
           while val2>val1:
              count=index2-index1+1
              if count<maxm:
                 maxm=count
              val2-=arr[index1]
              index1+=1
        index2+=1
    return maxm

if __name__=="__main__":
   print("============================")
   arr=[1,4,45,6,0,19]
   maxm=smallest_subarray(arr,51)
   print(f"The smallest subarray is {maxm}")
   print("=============================")
   brr=[1,10,5,2,7]
   maxm=smallest_subarray(brr,9)
   print(f"The smallest subarray is {maxm}")
   print("=============================")
   crr=[1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
   maxm=smallest_subarray(crr,280)
   print(f"The smallest subarray is {maxm}")
   print("=============================")
   

           
        

        
         
def minm_platforms(arr,dep):
    arr.sort()
    dep.sort()
    counter=0
    maxm=0
    index1=0
    index2=0
    while index1<len(arr) and index2<len(arr):
       if arr[index1]<dep[index2]:
          counter+=1
          if counter>maxm:
             maxm=counter
          index1+=1
       elif arr[index1]>dep[index2]:
          counter-=1
          index2+=1
    return maxm

if __name__=="__main__":
   print("====================================")
   arr=[900,940,950,1100,1500,1800]
   dep=[910,1200,1120,1130,1900,2000]
   print("The minimum platforms required is:")
   platforms=minm_platforms(arr,dep)
   print(f"The minimum platforms required is {platforms}")
   print("====================================")
   
      
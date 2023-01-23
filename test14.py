def find_pair(arr,target):
    arr.sort()
    index1=0
    index2=len(arr)-1
    while index1<index2:
        sm=arr[index1]+arr[index2]
        if sm==target:
           return index1,index2
        if sm>target:
           index2-=1
        if sm<target:
           index1+=1
    return -1,-1

if __name__=="__main__":
   print("=====================")
   arr=[10,20,35,50,75,80]
   index1,index2=find_pair(arr,70)
   print(index1,index2)
   print("======================")
        
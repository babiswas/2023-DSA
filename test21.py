def first_negative(arr,K):
    queue=list()
    index1=0
    index2=0
    while index1<len(arr) and index2<len(arr) and index1<=index2:
          if arr[index2]<0:
             queue.append(arr[index2])
          if index2-index1+1==K:
             print(arr[index1:index2+1])
             if not queue:
                print(0)
             else:
                num=queue[-1]
                print(num)
                if num==arr[index1]:
                   queue.pop(0)
             index1+=1
          index2+=1
if __name__=="__main__":
   print("============================")
   print("First negative number in the subarray of size K")
   arr=[-8,2,3,-6,10]
   first_negative(arr,3)
   print("=============================")
   
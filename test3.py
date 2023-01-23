def rearrange(arr,index):
    for i in range(len(arr)):
        index[i]=arr[index[i]]
    for i in range(len(arr)):
        arr[i]=index[i]



if __name__=="__main__":
   print("======================")
   arr=[10,11,12]
   index=[1,0,2]
   rearrange(arr,index)
   print(arr)
   print("==========================")
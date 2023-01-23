def reconstruct(arr):
    def update(D,l,r,num):
        D[l]=D[l]+num
        D[r+1]=D[r+1]-num

    D=[0]*(len(arr)+1)
    brr=[0]*(len(arr))
    #difference array
    for i in range(len(arr)):
       if i==0:
          D[i]=arr[i]
       else:
          D[i]=arr[i]-arr[i-1]
    #reconstruct an array
    update(D,0,1,10)
    update(D,1,3,20)
    update(D,2,2,30)
    for i in range(len(arr)):
        if i==0:
           brr[i]=D[i]
        else:
           brr[i]=D[i]+D[i-1]
           D[i]=D[i]+D[i-1]

    return brr

if __name__=="__main__":
   print("========================")
   arr=[10,5,20,40]
   brr=reconstruct(arr)
   print(brr)
   print("===========================")

import sys
def find_k_unique_substr(arr,k):
    mp=dict()
    index1=0
    index2=0
    count=0
    maxm=-sys.maxsize
    while index1<len(arr) and index2<len(arr) and index1<=index2:
          count=mp.get(arr[index2],-1)
          if count==-1:
             mp.update({arr[index2]:1})
             count+=1
          else:
             mp.update({arr[index2]:count+1})
          if len(mp)>k:
             cnt=mp.get(arr[index1],-1)
             if cnt!=-1:
                 mp.update({arr[index1]:cnt-1})
                 if mp[arr[index1]]==0:
                    del mp[arr[index1]]
                    count-=1
             index1+=1
          if len(mp)==k:
             if index2-index1+1>maxm:
                maxm=index2-index1+1
          index2+=1
    return maxm
if __name__=="__main__":
   print("==================================")
   print("Find k unique character in substring")
   maxm=find_k_unique_substr(list("aabbcc"),3)
   print(maxm)
   print("====================================")
   
   
   
 
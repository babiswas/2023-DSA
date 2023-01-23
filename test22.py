def find_anagram_k(arr,str1,k):
    mp=dict()
    for i in str1:
       count=mp.get(i,0)
       mp.update({i:count+1})
    print(mp)
    index1=0
    index2=0
    count=len(mp)
    ans=0
    while index1<len(arr) and index2<len(arr) and index1<=index2:
          cnt=mp.get(arr[index2],-1)
          if cnt!=-1:
             mp.update({arr[index2]:cnt-1})
          if cnt==0:
             count-=1
          if index2-index1+1==k:
             if count==0:
                ans+=1
             cnt=mp.get(arr[index1],-1)
             if cnt!=-1:
                mp.update({arr[index1]:cnt+1})
                if cnt==0:
                   count+=1
             index1+=1
          index2+=1
    return ans 

if __name__=="__main__":
   print("==========================")
   print("Count the number of anagram in a subarray of length K:")
   count=find_anagram_k(list("forxxorfxdofr"),list("for"),3)
   print(count)
   print("=============================")
   

             
          
             
          
          

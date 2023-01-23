def alt_pos_neg(arr):
   index=-1
   for i in range(len(arr)):
      if arr[i]<0:
         index+=1
         arr[index],arr[i]=arr[i],arr[index]
   print(arr)
   print(index)
   index1=0
   index2=index+1
   while index2<len(arr) and index1<index2 and arr[index1]<0:
         arr[index1],arr[index2]=arr[index2],arr[index1]
         index1+=2
         index2+=2
   return arr

if __name__=="__main__":
   print("==========================")
   print("Alternate positive and negative numbers:")
   arr=[-1,2,-3,4,5,6,-7,8,9]
   alt_pos_neg(arr)
   print(arr)
   print("===========================")
   
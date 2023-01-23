import sys
def buy_sell(arr):
   profit=-sys.maxsize
   buy=0
   sell=0
   for i in range(len(arr)-1):
      for j in range(i+1,len(arr)):
         if arr[j]-arr[i]>profit:
            profit=arr[j]-arr[i]
            buy=arr[i]
            sell=arr[j]
   print(f"Best time to buy the stock is {buy}")
   print(f"Best time to sell the stock is {sell}")
   print(f"Profit from the stock is {profit}")


def best_buy_sell(arr):
    buy=0
    sell=0
    maxm=-sys.maxsize
    minm=sys.maxsize
    profit=-sys.maxsize
    for i in range(len(arr)):
      if arr[i]<minm:
         minm=arr[i]
      if arr[i]>minm:
         if arr[i]-minm>profit:
            profit=arr[i]-minm
            buy=minm
            sell=arr[i]
    print(f"The buying price is {minm}")
    print(f"The selling price is {arr[i]}")
    print(f"Profit earned is {profit}")
      
       

if __name__=="__main__":
   print("====================================")
   print("Best time to buy and sell the stock is:")
   arr=[10,22,5,75,65,80]
   buy_sell(arr)
   print("======================================")
   print("Best time to buy and sell the stock is:")
   arr=[10,22,5,75,65,80]
   best_buy_sell(arr)
   print("======================================")
   
       
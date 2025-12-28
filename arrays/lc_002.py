# Best time to buy and sell stonks

def minmax():    
    prices =[7,6,4,3,1]
    last_profit=0
    

    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            
            profit=prices[j]-prices[i]
            print(profit)
    
minmax()
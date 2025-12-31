# Best time to buy and sell stonks

def minmax():    
    prices =[7,9,3,7,1]
    max_profit=0
    min_price=prices[0]

    for i in range(1,len(prices)):
            
            profit=prices[i]-min_price
    
            if profit > max_profit:
                max_profit=profit
                
            if prices[i] < min_price:
                min_price=prices[i]
        
    return max_profit
            
        
print(minmax())
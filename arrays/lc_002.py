# Best time to buy and sell stonks

def Profit():    
    
    """
    So my first intuition was to find the minimum value in the array from index 0 and then find the maximum value after it and the subtract them both
    clearly it did not work, so dont treat this question as a maximum minimum array problem.
    
    After that I tried to calculate every possible profit ever made every day and then finding the maximum profit, but it makes the time complexity O(N)^2
    and for large arrays makes the computation time consuming thus exceeding the time constrainst set by leet code.
    
    now what this code does is assume that the minimum price to start must be in the first index of the array, and it sets maximum profit to 0 as the problem description says
    after that it starts the loop from index number 1, and it subtracts the minimum value index 0 from index 1 to get the first profit, if the profit is greater than
    0 which it will be most of the times, except when we get a negative number
    """
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
            
        
print(Profit())
# Maximum Subarray Problem

def maxSubArray():
    """
    First we set the current max value and over_all_max value to the 0th index value, because when startring out at 0th index there is 
    only one subarray possible after that in the 1st iteration we add the current_maximum_value at 0th index with 1st index value, 
    now for the next step we check if the current_max_value is greater or less than the value at 1st index, if current_max_value 
    (sum of 0th and 1st index value) is less than the value at 1st index, we update the current_max_value with the value at 1st index,
    this is done so as to forget the past if it is not contributing positively, we give the subarray a fresh start, otherwise we wont 
    be able to find the maximum subarray, if current_max_value (sum of 0th and 1st index value) is not less than the 1st index value we 
    keep it, because it should help us in maximizing the subarray sum, now we compare the over_all_max_value with the current_max_value 
    in order to find the global maximum subarray sum, simply by comparing.
    
    
    Time Complexity : O(N)
    Space Complexity : O(1)
    
    """

    nums = [5,4,-1,7,8]
    sum=0
    current_max_value=nums[0]
    over_all_maximum=nums[0]


    for i in range(1,len(nums)):
        current_max_value = current_max_value + nums[i]
        
        if current_max_value < nums[i]:
            current_max_value=nums[i]

        
        if current_max_value > over_all_maximum:
            over_all_maximum=current_max_value
    return(over_all_maximum)

print(maxSubArray())
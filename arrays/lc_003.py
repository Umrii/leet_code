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
print(over_all_maximum) 
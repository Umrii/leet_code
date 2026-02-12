 

# number = 1234
# x=number
# rev_number=0
# while x>0:
#     rev=x%10
    
#     rev_number=rev_number*10+rev
#     x=x//10
    
# print(rev_number)

# nums =[1,4,9]
# comp_number=0

# for i in range(len(nums)):
#     comp_number=comp_number*10+nums[i]
    
# comp_number=comp_number+1


# for i in range(len(nums) - 1, -1, -1):
#     nums[i]=comp_number%10
#     comp_number=comp_number//10


# if comp_number > 0:
#     nums.insert(0, comp_number) # Normally, after refilling all positions, comp_number becomes 0, in case of [9] or [9,9] it inserts the remaining carry at the front.
    
# print((nums))

nums=[9,9,9]
def plusOne(nums):
    for i in range(len(nums)-1, -1, -1):
        if nums[i] < 9: # is the last index value is 9, we set it to zero, and move left and add 1 in the second last index value
            nums[i] += 1
            return nums
        nums[i] = 0

    return [1] + nums # this only runs when we have [9] or [9,9] or [9,9,9], you get the idea
print(plusOne(nums))
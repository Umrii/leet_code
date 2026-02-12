 

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
#     nums.insert(0, comp_number)
    
# print((nums))

nums=[9,9,9]
def plusOne(nums):
    for i in range(len(nums)-1, -1, -1):
        if nums[i] < 9:
            nums[i] += 1
            return nums
        nums[i] = 0

    return [1] + nums
print(plusOne(nums))
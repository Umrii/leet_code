#Shift Zeros to the Right
nums = [0,1,0,3,12]

for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i]==0:
            temp=nums[j]
            nums[j]=nums[i]
            nums[i]=temp


print(nums)


# nums = [0,1,0,3,12]

# for i in range(len(nums)):
#     # for j in range(i,len(nums)):
#         print(i,i+1)
#         # if nums[i]==0:
#         #     temp=nums[j]
#         #     nums[j]=nums[i]
#         #     nums[i]=temp


# # print(nums)


def fizzBuzz(n):
    
    for i in range(n+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)

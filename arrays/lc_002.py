# Best time to buy and sell stonks


prices = [7,6,4,3,1]
# print(len(prices)-1)

min=prices[0]
temp=0
day=0

for i in range(len(prices)-2):
        if min > prices[i+1]:
            min=prices[i+1]
            day=i+1
print(day,min)
max=0
day2=0
for i in range(day+1,len(prices)-1):
    # print(i)
    if max < prices[i]:
        max=prices[i]
        day2=i
print(day2,max)




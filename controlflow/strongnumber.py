#program for strong number


num=int(input("Enter a number : "))
temp=num
totalsum=0
while temp > 0:
    remainder=temp%10
    sum=1
    while remainder>1:
        sum=sum * remainder
        remainder -=1
    totalsum=sum+totalsum
    temp =temp // 10

if (totalsum == num):
    print(f"{num} is strong")
else:
    print(f"{num} is not strong.")

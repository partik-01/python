
#program to check for armstrong number

num=int(input("Enter a number : "))
#no. of digit
i=0
sum=0
rem=0
temp=num
while temp>0:
    i +=1
    temp =temp//10
temp=num
#checking
while temp>0:
    rem=temp%10
    sum=sum+pow(rem,i)
    temp =temp//10
if sum == num :
    print(f" {num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number. ")


#palindrome number

num=int(input("Enter a number :  "))
temp=num
reverse=0
while temp>0:
    rem=temp%10
    reverse=reverse *10 + rem
    temp=temp//10
if (reverse == num):
    print(f"{num} is palindrome number. ")
else:
    print(f"{num} is not a palindrome number. ")

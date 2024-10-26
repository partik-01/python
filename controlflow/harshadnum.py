
# program for checling harshad number 
#A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.



num= int(input("Enter a number: "))

digit_sum = 0
temp = num

while temp > 0:
    digit_sum += temp % 10  
    temp = temp // 10       

if num % digit_sum == 0:
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")


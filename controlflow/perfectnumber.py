
#proram for checking perfect number
num = int(input("Enter a number: "))

divisor_sum = 0

for i in range(1, num):
    if num % i == 0:
        divisor_sum += i

if divisor_sum == num:
    print(f"{num} is a Perfect number.")
else:
    print(f"{num} is not a Perfect number.")


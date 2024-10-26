#generate fibonacci series

num=int(input("Enter a number (>0): "))
first_term=1
second_term=1
print(f"The fibonnaci series up to {num} is ")
print(0)
print(first_term)
for i in range(1,int(num/2)):
    print(second_term)
    first_term=second_term+first_term
    print(first_term)
    second_term=second_term+first_term

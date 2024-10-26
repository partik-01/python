#checking if a number is fibonnaci number 
#using perfect square method
 
num=int(input("Enter a number : "))
check_num1=(5*pow(num,2)+4)
check_num2=(5*pow(num,2)-4)
temp1=int(pow(check_num1,0.5))
temp2=int(pow(check_num2,0.5))
if check_num1==pow(temp1,2) or check_num2==pow(temp2,2):
    print(f"{num} is fibonnaci number.")
else:
    print(f"{num} is not fibonnaci number .")



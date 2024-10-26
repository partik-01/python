
#program to check twin number

num=int(input("Enter a number(upto which twin number is to be checked): "))
prime_list=[]
for i in range (1,num+1):
    t=0
    for x in range(2,i):
        if i%x==0:
            t +=1
            break
    if t== 0 :
        prime_list.append(i)
print(prime_list)
for i in range (1,len(prime_list)):
    if (prime_list[i] - prime_list[i-1] )== 2:
        print(f"({prime_list[i-1]},{prime_list[i] })")



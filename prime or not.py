num=int(input("enter the number: "))
i=2
while i<num:
    if num%i==0:
        break;
i=i+1
if num==i:
    print(f"is prime number")
else:
    print(f"is not prime number")
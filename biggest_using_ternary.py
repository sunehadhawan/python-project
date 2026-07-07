a=int(input("enter first number: "))
b=int(input("enter second number: "))
print(f"a is biggest") if a>b else print(f"b is biggest")
biggest=a if a>b else b
print(f"biggest number is {biggest}")
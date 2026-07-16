num=int(input("enter a number: "))
for i in range(1,11,1):
    print(f"{num}x{i}={i*num}")
    for i in range(10,0,-1):
        print(i)
num=int(input("enter the number of rows"))
for row in range(num):
    a=row+1
    b=num-1
    for col in range(row+1):
        print(a,end=" ")
        a=a+b
        b=b-1
    print()
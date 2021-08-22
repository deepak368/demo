
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

prime=[]
if number1<number2:
    for k in range(number1, number2 + 1):
        if k > 1:
            for i in range(2, k):
                if (k % i) == 0:
                    break
            else:
                print(k)
                prime.append(k)
    print("sum of prime=",sum(prime))

if number1>number2:
    print("please enter the first number as lower than the second number")

if number1==number2:
    print("there is no numbers between ",number1,"and",number2 )
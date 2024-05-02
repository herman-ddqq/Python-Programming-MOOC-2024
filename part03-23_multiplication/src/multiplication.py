number = int(input("Please type in a number: "))
a = 1
b = 1

while a <= number:
    while b <= number:
        result = a*b
        print (f"{a} x {b} = {result} ")
        b+=1
    b=1
    a+=1
    continue
# Write your solution here
#Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.
print("Please type in integer numbers. Type in 0 to finish.")
quantity = 0
SUM=0
MEAN=0
POS=0
NEG=0

while True:
    number = int(input("Number: "))
    quantity +=1
    SUM += number
    MEAN = SUM/quantity

    if number == 0:
        quantity-=1
        SUM-=0
        MEAN = SUM/quantity
        break

    if number <0:
        NEG+=1
    
    if number >0:
        POS+=1


print ("... the program asks for numbers")
print (f"Numbers typed in {quantity}")
print (f"The sum of the numbers is {SUM}")
print (f"The mean of the numbers is {MEAN}")
print (f"Positive numbers {POS}")
print (f"Negative numbers {NEG}")

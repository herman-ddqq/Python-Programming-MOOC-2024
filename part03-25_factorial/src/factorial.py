while True:
    number = int (input("Please type in a number: "))
    i = 1
    factorial = 1
    if number <= 0:
        print ("Thanks and bye!")
        break
    while i <= number:
        factorial = factorial*i
        i+=1
        continue
    print(f"The factorial of the number {number} is {factorial}")
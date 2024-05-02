# Write your solution here
year = int(input("Year: "))
NEXT = int(year + 1)
while True:
    if NEXT % 4 == 0 and NEXT % 100 != 0:
        break
    
    elif NEXT % 100 == 0 and NEXT % 400 == 0:
        break

    else:
        NEXT = NEXT + 1
  
print (f"The next leap year after {year} is {NEXT}")





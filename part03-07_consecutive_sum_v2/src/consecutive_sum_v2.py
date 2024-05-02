# Write your solution here
limit = int(input("Limit: "))
summ = 0  
number = 1
calculation_string = ""

while summ < limit:
    calculation_string += f"{number} + "
    summ += number 
    number += 1 

calculation_string = calculation_string[:-3]

print (f"The consecutive sum: {calculation_string} = {summ}")

# Write your solution here
wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
dayweek = input("Day of the week: ")
dailywage_regular = (wage*hours)
dailywage_sunday = (wage*hours*2)

if dayweek=="Sunday":
        print (f"Daily wages: {dailywage_sunday} euros")

if dayweek!="Sunday":
        print (f"Daily wages: {dailywage_regular} euros")

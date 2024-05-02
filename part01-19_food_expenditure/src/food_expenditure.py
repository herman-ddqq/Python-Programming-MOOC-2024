# Write your solution here
eat_times = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
money_spend = float(input("How much money do you spend on groceries in a week? "))
daily_exp = float((eat_times*lunch_price+money_spend)/7)
weekly_exp = float(eat_times*lunch_price+money_spend)

print ("Average food expenditure:")
print (f"Daily: {daily_exp} euros")
print (f"Weekly: {weekly_exp} euros")
# Write your solution here
print ("What is the weather forecast for tomorrow? ")
temperature = int(input("Temperature: "))
RAIN = input("Will it rain (yes/no): ")

if temperature>=20:
    print("Wear jeans and a T-shirt")

if temperature<=20:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")

if temperature<=10:
    print("Take a jacket with you")

if temperature<=5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if RAIN=="yes":
    print("Don't forget your umbrella!")

if RAIN=="no":
    print()
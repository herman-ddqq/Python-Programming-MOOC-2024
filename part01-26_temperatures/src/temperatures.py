# Write your solution here
temperatureF = int(input("Please type in a temperature (F): "))
temperatureC = float((temperatureF-32)*5/9)

if temperatureC>=0:
        print (f"{temperatureF} degrees Fahrenheit equals {temperatureC} degrees Celsius")


if temperatureC<0:
        print (f"{temperatureF} degrees Fahrenheit equals {temperatureC} degrees Celsius")
        print ("Brr! It's cold in here!")
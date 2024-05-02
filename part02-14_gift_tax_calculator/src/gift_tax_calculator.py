# Write your solution here
gift_value = int(input("Value of gift: "))

if 5000<=gift_value<25000:
    taxLOWER=100
    giftLOWER=5000
    taxRATE=0.08

elif 25000<=gift_value<55000:
    taxLOWER=1700
    giftLOWER=25000
    taxRATE=0.1

elif 55000<=gift_value<200000:
    taxLOWER=4700
    giftLOWER=55000
    taxRATE=0.12

elif 200000<=gift_value<1000000:
    taxLOWER=22100
    giftLOWER=200000
    taxRATE=0.15

elif gift_value>=1000000:
    taxLOWER=142100
    giftLOWER=1000000
    taxRATE=0.17

else:
    taxLOWER=0
    giftLOWER=0
    taxRATE=0
    tax_amount=0

tax_amount=(taxLOWER+(gift_value-giftLOWER)*taxRATE)

if tax_amount==0:
    print ("No tax!")
else:
    print (f"Amount of tax: {tax_amount}")



food = input("enter food: ")
number = int(input("how many? "))

if food == "pizza":
    price = 250000
elif food == "burger":
    price = 180000
elif food == "sandwich":
    price = 120000
else:
    print("not available on the menu!")

if food == "pizza" or food == "burger" or food == "sandwich":
        total = price * number
        print("total:" , total)

        if total > 500000:
            print("ur getting a free drinkk🥤")


age = int(input("enter age: "))
day = input("enter day: ")

price = 200000

if age < 12:
    price = price * 0.5
elif age >= 60:
    price = price * 0.7
elif day == "3shanbe":
    price = price * 0.8

    print("final price: " , price)


price= float(input("enter ur price: "))
shipping= input("enter ur shipping type: ")

if shipping == "عادی":
    if price > 2000000:
        print("shipping is free")
    else:
        print(price + 50000)
elif shipping == "سریع":
    print(price + 100000)
else:
    print("invalid shipping type!")
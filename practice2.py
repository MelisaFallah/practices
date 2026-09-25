

distance= float(input("enter distance in kilometers: "))

price = 30000 + (distance * 8000)
print("ur fare:" , price)

if 20<distance:
    off = price * 0.05
    price = price - off
    print("ur fare with discount: " , price)
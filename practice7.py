

weight = float(input("enter ur weight (km) : "))
height = float(input("enter ur height (m) : "))

if weight <= 0 or height <= 0:
    print("invalid input!")
else:
    bmi = weight / (height ** 2)
    print("ur BMI:" , bmi)
    if bmi < 18.5:
        print("underweight")
    elif bmi < 25:
        print("normal")
    elif bmi < 30:
        print("overweight")
    else:
        print("obesity🫢")

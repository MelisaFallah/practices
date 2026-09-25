

age= int(input("inter ur age: "))
print(age)
    
if 18>age:
    print("Bye Bye💋")
elif 18<=age:
    username= input("type ur username: ")
    password= input("type ur password: ")
    if username == "dark shadow" and password == "king arthur 7300":
        print("login")
    elif username == "dark shadow" and password != "king arthur 7300":
        print("wrong password!")
    elif password == "king arthur 7300" and username != "dark shadow":
        print("wrong username!")
    elif username != "dark shadow" and password != "king arthur 7300":
        print("both r wrong!!!")
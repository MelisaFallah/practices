

password = input("password: ")
balance = float(input("balance: "))
withdraw = float(input("withdraw: "))

if password != "1234":
    print("wrong password!")
elif withdraw <= 0:
    print("invalid amount!")
elif withdraw % 50000 != 0:
    print("amount must be multiple of 50000")
elif withdraw > balance:
    print("balance not enough!!!")
else:
    print("new balance: " , balance - withdraw)

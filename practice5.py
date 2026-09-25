

balance = float(input("enter ur balance: "))
withdraw = float(input("enter ur withdraw amount: "))

if withdraw <= 0:
    print("invalid withdraw")

elif balance < withdraw :
    print("not enough balance")

elif balance - withdraw < 100000:
    print("WARNING!!!")

else:
    print(balance - withdraw)
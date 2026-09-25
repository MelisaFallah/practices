

temp = float(input("enter the temp: "))

if temp < 0 :
  print("wear sth thick")
elif 0<=temp<=10 :
  print("wear sth warm")
elif 11<=temp<=25 :
  print("such a nice day")
elif temp>25 :
  print("wear sth light")

rain = input("is it raining? ")
if rain == "yes":
  print("take an umbrella")

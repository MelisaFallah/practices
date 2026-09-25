

usage = int(input("enter ur elec usage: "))

if usage<=100:
    print(usage * 1000)
elif 101<=usage<=200:
    print(usage * 1500)
elif usage>200:
    print(usage * 2500)
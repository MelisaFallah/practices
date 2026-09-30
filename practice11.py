

students = []
grades = []
number = int(input("How many students? "))

for i in range (number):
    name = input("enter ur name: ")
    grade = float(input("enter ur grade: "))

    students.append(name)
    grades.append(grade)

username = input("enter ur username: ")
password = input("enter ur password: ")

if username == "admin" and password == "1234":
    while True:
        print("1.show students 2.show grades 3.exit")

        choice = input("choose: ")
        if choice == "1":
            print(students)
        elif choice == "2":
            print(grades)
        elif choice == "3":
            print("ByeBye")
            break
        else:
            print("invalid choice!")
else:
    print("Wrong username or password!")

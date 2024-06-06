# name = input("what is your name?")
# year = input("what year were you born?")
# print(" hello " + name +", nice to meet you." )
# print("hello world")

# Assignment
# This is wrong
# Firstname = input("Praise")
# Lastname = input("Amayo")
# Yearofbirth = input("1994")
# print("Hello Praise Amayo " +", you are 30years old!")


# Correct
# from datetime import datetime
# birth_date = datetime(1994, 9, 14)
# today = datetime.today()
# First_name  = input("what is your first name?")
# Last_name = input("what is your last name?")
# Year_of_birth = input("what is your year of birth?")
# Current_year = 2024
# Current_age = Current_year - abs(int(Year_of_birth))
# print(f"Hi  {First_name} {Last_name}, you are {Current_age} years old")


# Number guessing game
# import random 
# r = random.randrange(1, 10)
#  attempts = 5

# while attempts > 0:  
#     guess = int(input("make your guess:"))
#     if guess > R:
#        print("Too high")
#     elif guess < R:
#          print("Too low")
#     else: 
#          print("you guessed it right!!")
#          break
#     attempts -=1
    # if attempts > 0:
    #     print("you 've used all your attempts. The number was{R}.")
  

#   LECTURE 4

# def test():
#     global food
#     food  = ['eba', 'amala', 'indomie', 'eggs']
#     for i in range(len(food)):
#         print(i,food[i])

# test()
# # print(food)

# def area(Length,breadth):
#     return Length*breadth
# print(area(4,5))

# class work
# def interest(P,R,T):
#     return P*R*T/100
# print(interest(4,5,6)) 

# # Assignment
# def calculate_interest(principal:int, rate:int, time):
#     if rate > 100:
#         print("Rate must not exceed 100")
#         return
#     if time > 12:
#         time = time / 12
#         interest = (principal * rate * time) / 100
#         return interest
    
# print(calculate_interest(40,10,13))


# # ASSIGNMENT:
# def count_movies_by_genre(movies):
#     genre_count = {}
#     for movie in movies:
#         genres = movie.get("genres", [])
#         if genre in genres:
#             genre_count[genre] + 1
#         else:genre_count[genre] = 1

#     return genre_count
# movies = [
#     {"title": "World apart", "genres": ["genre", "Adventure"]},
#     {"title": "A night with the king", "genres": ["Drama"]},
#     {"title": "Best friend for ever", "genres": ["Comedy", "Romance"]},
#     {"title": "Love me no more", "genres": ["Action", "Thriller"]},
#     {"title": "Heaven sent", "genres": ["Adventure", "Drama"]},
# ]

# print(count_movies_by_genre(movies))


# lol = [0, 1, 2, 3, 4, 5, 6]
# lol.sort()
# print(lol)




class Employee:
    def _init_(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

class company:
    def _init_(self):
        self.employees = []

    def add_employee(self):
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        position = input("Enter employee position: ")
        salary = float(input("Enter employee salary: "))
        employee = Employee(name, age, position, salary)
        self.employees.append(employee)
        print("Employee added successfully!")

    def remove_employee(self):
        name = input("Enter employee name to remove: ")
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print("Employee removed successfully!")
                return
        print("Employee not found.")

    
    def update_employee(self):
        name = input("Enter employee name to update: ")
        for employee in self.employees:
            if employee.name == name:
                employee.position = input("Enter new position: ")
                employee.salary = float(input("Enter new salary: "))
                print("Employee updated successfully!")
                return
        print("Employee not found.")

    def view_all_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}, Age: {employee.age}, Position: {employee.position}, Salary: {employee.salary}")

    def find_employee_by_name(self):
        name = input("Enter employee name to find: ")
        for employee in self.employees:
            if employee.name == name:
                print(f"Name: {employee.name}, Age: {employee.age}, Position: {employee.position}, Salary: {employee.salary}")
                return
        print("Employee not found.")

def user_interface():
    ems = company()
    while True:
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Update employee")
        print("4. View all employees")
        print("5. Find employee by name")
        print("6. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            ems.add_employee()
        elif choice == "2":
            ems.remove_employee()
        elif choice == "3":
            ems.update_employee()
        elif choice == "4":
            ems.view_all_employees()
        elif choice == "5":
            ems.find_employee_by_name()
        elif choice == "6":
            break
        else:
            
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    user_interface()
    











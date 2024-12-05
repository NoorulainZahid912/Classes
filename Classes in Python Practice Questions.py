#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# NOOR UL AIN ZAHID
# FA24-BBD-069 (BDA-A)


# In[ ]:


# Practice Exercises:


# In[1]:


# 1. Create a class Person with attributes name, age, and city.
class person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
        
    def display_name(self):
        print(f"My name is {self.name} .")
        
    def display_age(self):
        print(f"My age is {self.age} .")
        
    def display_city(self):
        print(f"My city name is {self.city}.")
        
# Creating an object of the class        
Person=person("Noor ul Ain Zahid",19,"Lahore")

# Calling the methods using the object instance
Person.display_name()
Person.display_age()
Person.display_city()


# In[3]:


# 2. Create a class Car with attributes make, model, and year. 

# Define the Car class
class Car:
   
 # Initialize the class with attributes
    def __init__(self,make,model,year):
        self.make = make
        self.model = model 
        self.year = year
        
# Method to display car details 
    def display_make(self):
        print(f"I will own {self.make} in future." )
    def display_model(self):    
        print(f"Its current model is {self.model} but i will own its latest model in future.")
    def display_year(self):
        print(f"Its current model is of year {self.year}.")
        
# Create an instance (object) of the Car class
car=Car(" Lamborghini", "Aventador",2024)

# Calling the methods using the object instance
car.display_make()
car.display_model()
car.display_year()


# In[6]:


# 3. Create a class Circle with attributes radius and methods to calculate area and circumference.
class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.area = 3.14*self.radius**2  # Calculate area
        self.circumference = self.radius*3.14*2   # Calculate circumference
        
# Method to display the area of the circle    
    def display_area(self):    
        print(f"The area of the circle is {self.area}.")
        
# Method to display the circumference of the circle        
    def display_circumference(self):
        print(f"The circumference of the circle is {self.circumference}.")
        
# Create an object of Circle class with radius 6        
circle = Circle(6)

# Display area and circumference
circle.display_area()
circle.display_circumference()


# In[ ]:


# 4. Create a class Rectangle with attributes length and width and methods to calculate area and perimeter.
class Rectangle:
    # Initialize the class with length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.length * self.width  # Area formula: length * width
        self.perimeter = 2 * (self.length + self.width)  # Perimeter formula: 2 * (length + width)
    
    # Method to display the area of the rectangle
    def display_area(self):
        print(f"The area of the rectangle is {self.area}.")
    
    # Method to display the perimeter of the rectangle
    def display_perimeter(self):
        print(f"The perimeter of the rectangle is {self.perimeter}.")

# Create an object of Rectangle class with length 5 and width 3
rectangle = Rectangle(5, 3)

# Display area and perimeter
rectangle.display_area()
rectangle.display_perimeter()


# In[7]:


# 5.Create a class Student with attributes name, roll_number, and marks. Implement a method to calculate the average marks.
class Student:
    # Initialize the class with name, roll_number, and marks
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  # A list of marks obtained in different subjects
        self.average = self.calculate_average()  # Calculate average marks
    
    # Method to calculate the average marks
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)  # sum(marks) / number of subjects
    
    # Method to display student information
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Average Marks: {self.average:.1f}")

# Create an object of the Student class
student = Student("Noor Ul Ain Zahid", "069", [40, 21, 21, 20, 17,17,10,26])

# Display student information
student.display_info()


# In[9]:


# 6. Create a class Book with attributes title, author, and publication_year.
class Book:
    # Initialize the class with title, author, and publication_year
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    
    # Method to display book details
    def display_info(self):
        print(f"My favourite book is '{self.title}'")
        print(f"The Author of this book is '{self.author}'")
        print(f"Its Publication Year is {self.publication_year}")

# Create an object of the Book class
book = Book("The Alchemist", "Paulo Coelho", 1988)

# Display book information
book.display_info()


# In[10]:


# 7. Create a class Employee with attributes name, salary, and designation.
class Employee:
    # Initialize the class with name, salary, and designation
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
    
    # Method to display employee details
    def display_info(self):
        print(f"I have an employee '{self.name}' in my office.")
        print(f"Her salary is Rs.{self.salary} per month.")
        print(f"Her designation is '{self.designation}' .")

# Create an object of the Employee class
employee = Employee("Layan", 100000, "Data Analyst")

# Display employee information
employee.display_info()


# In[15]:


# 8. Create a class Bank with attributes name, account_number, and balance. Implement methods to deposit and withdraw money.
class Bank:
    def __init__(self, name, account_number, balance=56780):
        # Initialize the account with name, account number, and balance
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        # Add money to the account balance
        if amount > 0:
            self.balance += amount
            print(f"Dear Layan! Deposited money in your account is Rs.{amount} .So, your new balance is Rs.{self.balance}")
        
    def withdraw(self, amount):
        # Subtract money from the account balance if there is enough balance
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Dear Layan! Withdrew amount from your account is Rs.{amount} .So, your new balance is Rs.{self.balance}")
       
    def show_balance(self):
        # Display current balance
        print(f"Dear Layan! Your current balance is Rs.{self.balance}")

# Create a Bank account object
account = Bank("Layan", "1234567890", 5000)

# Show the initial balance
account.show_balance()

# Deposit money
account.deposit(2000)

# Withdraw money
account.withdraw(3000)


# In[ ]:





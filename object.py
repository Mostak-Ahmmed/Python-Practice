# # Corrected version of the Employee class

# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello, my name is " + self.name)

# # Creating an instance of the Employee class
# e1 = Employee("John", 26)

# # Calling the method to display the message
# e1.myfunc()



# # Modify Object Properties
# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello, my name is " + self.name)

# # Create an instance of Employee
# e1 = Employee("John", 26)

# # Modify the 'age' property
# e1.age = 30
# print("Modified age:", e1.age)

# Output:
# Modified age: 30

# ---------------------------------------------------

# Delete Object Properties
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

# Create an instance of Employee
e1 = Employee("John", 26)

# Delete the 'age' property
del e1.age

# Attempting to print the 'age' property will raise an error
try:
    print("Deleted age:", e1.age)  # This will raise an AttributeError
except AttributeError as e:
    print("Error:", e)

# Output:
# Error: 'Employee' object has no attribute 'age'


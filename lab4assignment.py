# --------------------------------------------------------
# Lab 4: Python Practice - Group Assignment
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Annie Yung
# Date: 10/4/2024

import numpy as np

#checks if number is positive, negative, or zero
print("Exercise 1: Checks if a number is positive, negative, or zero")
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

print()
print()

#writing a for loop that prints every second number between 0 and 10
print("Exercise 2: Writing a loop that prints every second number from 0 to 10")
for i in range (0, 10+1):
   if(i%2==0):
      print(i)

print()

#while loops that prints numbers from 1 to 100
print("Exercise 3: While Loop that prints numbers 1 to 100")
n=1
while n <= 100:
   print(n, end=' ')
   n = n+1

print()
print()

#looping through rows and columns of a matrix
array = np.array([[0, 1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10, 11],
                  [12, 13, 14, 15, 16, 17],
                  [18, 19, 20, 21, 22, 23]])

for col in array.T:
   print(col)
   print()
   print()

for row in array.T:
   print(row)

print()
print()

#writing a function that takes two numbers as arguments and returns their sums
print("Exercise 5: Function that takes two numbers as arguments and returns their sums")
def add_numbers(a,b):
   return a+b

num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

result = add_numbers(num1, num2)
print("Sum of the two numbers:", result)

print()
print()

#writing a function that calculates the area of a rectangle, with a default length and width
print("Exercise 6: Function that calculates the area of a rectangle")
def area_rectangle(length, width):
   return length * width

num1 = float(input("Please enter the width of the rectangle: "))
num2 = float(input("Please enter the length of the rectangle: "))

result = area_rectangle(num1, num2)
print("The area of the rectangle is:", result)

print()
print()

#using the try-except method to handle user input errors in a calculator
print("Exercise 7: Using the try-except method for user input errors")
def add(x, y):
   return x + y


def subtract(x, y):
   return x - y


def multiply(x, y):
   return x * y


def divide(x, y):
   try:
      result = 10 / 0
   except ZeroDivisionError:
      print("ERROR: Dividing by zero")


def exponent(x, y):
   return x ** y


def mod(x, y):
   return x % y


def sqrt(x):
   return x ** (1 / 2)


# Defining user input for math operations
def main():
   while True:
      print("Please type in the math operation you would like to complete:")
      print("1. Add")
      print("2. Subtract")
      print("3. Multiply")
      print("4. Division")
      print("5. Exponents")
      print("6. Remainder value")
      print("7. Square root")
      print("8. Exit")
      print("9. Clear screen")

      choice = input("Enter choice: ")

      # if value == 8, then the loop will end

      if choice == '8':
         print("exiting, thank you!")
         break

      if choice == '9':
         break
         os.system('clear')

      if choice == '1':
         num1 = float(input("Enter your first number: "))
         num2 = float(input("Enter your second number: "))
         print(f"{num1} + {num2} = {add(num1, num2)}")
      elif choice == '2':
         num1 = float(input("Enter your first number: "))
         num2 = float(input("Enter your second number: "))
         print(f"{num1} - {num2} = {subtract(num1, num2)}")
      elif choice == '3':
         num1 = float(input("Enter your first number: "))
         num2 = float(input("Enter your second number: "))
         print(f"{num1} * {num2} = {multiply(num1, num2)}")
      elif choice == '4':
         num1 = float(input("Enter your first number: "))
         num2 = float(input("Enter your second number: "))
         print(f"{num1} / {num2} = {divide(num1, num2)}")
      elif choice == '5':
         num1 = float(input("Enter your first number: "))
         num2 = float(input("Enter your second number: "))
         print(f"{num1} ** {num2} = {exponent(num1, num2)}")
      elif choice == '6':
         num1 = float(input("Enter your first number: "))
         num2 = float(input("Enter your second number: "))
         print(f"{num1} %= {num2} = {mod(num1, num2)}")
      elif choice == '7':
         num1 = float(input("Enter your number: "))
         print(f"{num1} ** (1/2) = {sqrt(num1)}")
      elif choice == '9':
         clear_screen()
      else:
         print("Invalid input, please select a math operation again")


if __name__ == "__main__":
   main()


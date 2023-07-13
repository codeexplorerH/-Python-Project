# project-1 Simple Calculator for Calculation

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


print("--------- WELCOME TO S.CALCULATOR ---------")

print("please Select Operation-\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide")

print("select operation from 1,2,3,4")
select = int(input("Enter Operation :-"))

number_1 = int(input("Enter the First Number:"))
number_2 = int(input("Enter the Second Number:"))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif select == 3:
    print(number_1, "-", number_2, '*', multiply(number_1, number_2))

elif select == 4:
    print(number_1, "-", number_2, " \ ", divide(number_1, number_2))

else:
    print("Invalid Input")

print("Thank You For Using our S.Calculator")
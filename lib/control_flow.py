#!/usr/bin/env python3

def admin_login(username, password):
    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    # if betw 40 and 65
    elif temperature >= 40 and temperature<= 65:
    # return "It's a little chilly out there!"
        return "It's a little chilly out there!"
    # else if abv 85 rtn "It's too dang hot out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    # default "It's perfect out there!"
    else:
        return "It's perfect out there!"
    

def fizzbuzz(num):

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    
    elif num % 3 == 0:
        return "Fizz"

    elif num % 5 == 0:
        return "Buzz"
    
    else:
        return num




def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0: 
            return num1 / num2
        else:
            print("Cannot divide by zero!")
            return None
    else:
        print("Invalid operation!")
        return None


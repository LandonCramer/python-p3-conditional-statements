#!/usr/bin/env python3

# def admin_login(username, password):
#     if username.upper() == "ADMIN" and password =="12345":
#         return "Access granted"
    
#     return "Access denied"

# def hows_the_weather(temperature):
#     if temperature < 40:
#         return "It's brisk out there!"
#     elif temperature < 65:
#         return "It's a little chilly out there!"
#     elif temperature > 85:
#         return "It's too dang hot out there!"
#     else:
#         return "It's perfect out there!"


# def fizzbuzz(num):
#     if not num % 15:
#         return "FizzBuzz"
#     elif not num % 5:
#         return "Buzz"
#     elif not num % 3:
#         return "Fizz"
    
#     return num

# def calculator(operation, num1, num2):
#     if operation == "+":
#         return num1 + num2
#     elif operation == "-":
#         return num1 -num2
#     elif operation == "*":
#         return num1 * num2
#     elif operation == "/":
#         return num1 / num2
#     else:
#         print("Invalid operation!")
#         return None
#     pass


def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    elif username == "ADMIN" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    
# print(admin_login("sudo", "12345"))
# # "Access denied"
# print(admin_login("admin", "12345"))
# # "Access granted"
# print(admin_login("ADMIN", "12345"))
# # "Access granted"

def hows_the_weather(temp):
    if temp < 40:
        return "It's brisk out there!"
    elif temp < 65:
        return "It's a little chilly out there!"
    elif temp > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

# print(hows_the_weather(33))
# # "Brisk!"
# print(hows_the_weather(99))
# # "Too dang hot"
# print(hows_the_weather(75))
# # "Perfect!"

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number

# print(fizzbuzz(1))
# # 1
# print(fizzbuzz(2))
# # 2
# print(fizzbuzz(3))
# # Fizz
# print(fizzbuzz(4))
# # 4
# print(fizzbuzz(5))
# # Buzz
# print(fizzbuzz(15))
# # FizzBuzz

acceptable = ["+", "-", "*", "/"]

def calculator(operation, num1, num2):
    # Check if the operation is in the list of acceptable operations
    if operation not in acceptable:
        print("Invalid operation!")
        return None
    
    # Perform the appropriate arithmetic operation
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

print(calculator("+", 1, 1))
# 2
print(calculator("-", 3, 1))
# 2
print(calculator("*", 3, 2))
# 6print()
print(calculator("/", 4, 2))
# 2
print(calculator("nope", 4, 2))
# "Invalid operation!"
# None

#!/usr/bin/env python3

def admin_login(username, password):
    """
    Checks if username and password match admin credentials.
    Returns "Access granted" if username is "admin" or "ADMIN" and password is "12345".
    Otherwise returns "Access denied".
    """
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    """
    Returns a message based on the temperature.
    - Below 40: "It's brisk out there!"
    - Between 40 and 65: "It's a little chilly out there!"
    - Above 85: "It's too dang hot out there!"
    - Otherwise: "It's perfect out there!"
    """
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    """
    Classic FizzBuzz implementation.
    - Multiples of 3: return "Fizz"
    - Multiples of 5: return "Buzz"
    - Multiples of both 3 and 5: return "FizzBuzz"
    - Otherwise: return the number itself
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def calculator(operation, num1, num2):
    """
    Performs basic arithmetic operations.
    Valid operations: +, -, *, /
    Returns the result of the operation or None if operation is invalid.
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None


# Test the functions
if __name__ == "__main__":
    # Test admin_login
    print("Testing admin_login:")
    print(admin_login("sudo", "12345"))  # Access denied
    print(admin_login("admin", "12345"))  # Access granted
    print(admin_login("ADMIN", "12345"))  # Access granted
    
    # Test hows_the_weather
    print("\nTesting hows_the_weather:")
    print(hows_the_weather(33))  # It's brisk out there!
    print(hows_the_weather(99))  # It's too dang hot out there!
    print(hows_the_weather(75))  # It's perfect out there!
    
    # Test fizzbuzz
    print("\nTesting fizzbuzz:")
    print(fizzbuzz(1))   # 1
    print(fizzbuzz(2))   # 2
    print(fizzbuzz(3))   # Fizz
    print(fizzbuzz(4))   # 4
    print(fizzbuzz(5))   # Buzz
    print(fizzbuzz(15))  # FizzBuzz
    
    # Test calculator
    print("\nTesting calculator:")
    print(calculator("+", 1, 1))      # 2
    print(calculator("-", 3, 1))      # 2
    print(calculator("*", 3, 2))      # 6
    print(calculator("/", 4, 2))      # 2
    print(calculator("nope", 4, 2))   # Invalid operation! + None
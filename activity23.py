def check_divisibility(number):
    """
    Checks if a given number is divisible by both 3 and 5.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "The number is divisible by both 3 and 5."
    elif number % 3 == 0:
        return "The number is divisible by 3 but not by 5."
    elif number % 5 == 0:
        return "The number is divisible by 5 but not by 3."
    else:
        return "The number is neither divisible by 3 nor by 5."

try:
    user_input = int(input("Enter an integer: "))
    result = check_divisibility(user_input)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
def calculate_sum():
    try:
        num1 = float(input(Enter the first number: ))
        num2 = float(input(Enter the second number: ))
        result = num1 + num2
        print(fThe sum of {num1} and {num2} is: {result})
    except ValueError:
        print(Invalid input. Please enter valid numbers.)

if __name__ == __main__:
    calculate_sum()


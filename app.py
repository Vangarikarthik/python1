def calculate_sum():
    try:
        num1 = 59
        num2 = 10
        result1 = num1 + num2
        print("The sum  is:"+ result1)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == '__main__':
    calculate_sum()


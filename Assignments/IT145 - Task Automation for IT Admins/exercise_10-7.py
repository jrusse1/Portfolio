print("This program takes two numbers to add, then prints the result.")
while True:
    num1 = input("Please enter the first number:\n")
    num2 = input("Please enter the second number:\n")
    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print('You entered a letter. Please enter a number.')
    else:
        print('Answer:', answer)


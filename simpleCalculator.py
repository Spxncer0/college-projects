# Asking function
while True:
    function = input('1. Add\n2. Subtract\n3. Multiply\n4. Divide\nWhat function do you want to use? (Please enter the number): ')
    if function == '1' or function == '2' or function == '3' or function == '4':
        break
    else:
        print('\nPlease enter a valid number!\n')

# Asking numbers
while True:
    try:
        num1 = float(input('What is the first number?: '))
        num2 = float(input('What is the second number?: '))
        break
    except ValueError:
        print('Please enter a number!')
    

# Setting constants
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2

if function == '1':
    print(f'The answer is {add}!')

elif function == '2':
    print(f'The answer is {subtract}!')

elif function == '3':
    print(f'The answer is {multiply}!')

elif function == '4':
    print(f'The answer is {divide}!')
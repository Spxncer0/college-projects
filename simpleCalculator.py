# Asking function
while True:
    function = input('What function do you want to use?: (Please enter the number)\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n')
    if function == '1' or function == '2' or function == '3' or function == '4':
        break
    else:
        print('Please enter a valid number!')

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
    print(add)

elif function == '2':
    print(subtract)

elif function == '3':
    print(multiply)

elif function == '4':
    print(divide)
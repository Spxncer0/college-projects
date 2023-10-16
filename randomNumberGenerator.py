# Started 14/10/23

# Importing random module
import random

# Setting random number
number = random.randint(1,10)

# Guess number
while True:
  try:
    user_input = int(input('Guess a number between 1 and 10!: '))

# Successful input
    if user_input == number:
      print('Congrats! You guessed the right number!')

# Asking to retry after successful input
      while True:
        again = input('Would you like to try again? (y/n): ')

        if again == 'y':
          number = random.randint(1,10)
          break

        elif again == 'n':
          print('Have a good day!')
          exit()

        else:
          print('Please enter either y/n')
        continue

# Catching numbers outside range
    elif user_input >10 or user_input <1:
      print('Please enter a number that is between 1 and 10!')
    
# Lower
    elif user_input > number:
        print('Lower, try again!')
      
# Higher
    elif user_input < number:
        print('Higher, try again!')
      
# Incorrect input altogether (not a number)
    elif user_input != number:
      print('Wrong, Try again!')
      continue

# Catching input error
  except ValueError:
    print('Please enter a number!')
    continue
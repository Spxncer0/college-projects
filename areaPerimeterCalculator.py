# Started 14/10/2023

# Setting height and width of the rectangle
while True:
  try:
    height = int(input ('How tall is your rectangle in cm?: '))
    width = int(input ('How wide is you rectangle in cm?: '))
    break
  except ValueError:
    print('Please enter a number')
    continue

# Setting variables (formulas)
area = height * width
perimeter = ((height * 2) + (width * 2))

# Print the result in centimetres
print('The area of the rectangle is: ' + str(area)+'cm')
print('The perimeter of the rectangle is: ' + str(perimeter)+'cm')
print(' ')

# Asking user if they want the result converted to metres
converted = input('Do you want it converted into metres?: (y/n) ')
print(' ')

# Setting IF statements
if converted == 'y':

  # Setting variables for conversion (formulas)
  area_cm_to_m = area / 10
  perimeter_cm_to_m = perimeter / 10

  # Print the result in metres
  print('In metres the area of the rectangle is: ' + (str(area_cm_to_m))+'m')
  print('In metres the perimeter of the rectangle is: ' + (str(perimeter_cm_to_m))+'m')

  if converted == 'n':
    print(' ')

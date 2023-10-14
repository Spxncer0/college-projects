# Setting variables, with full caps = constant
temperature = int(input('Enter a temperature: '))
CELSIUS = temperature * 1.8 + 32
FARENHEIT = ((temperature - 32) / 1.8)

# Asking the user what metric the degrees is in
metric = input('In celsius or farenheit? (c/f): ')

# Printing the conversion depending on user input
if metric == 'c':
  print(CELSIUS)

elif metric == "f":
  print(FARENHEIT)
number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the first number: '))

# perform Addition
addition = number1 + number2

# perform subtraction
subtraction = number1 - number2

# perform multiplication
multiplication = number1 * number2


# perform division
if number2 != 0:
    division = number1 / number2
else:
    division = "undefined (cannot be divided by zero)"

# print section
print(f'The result of {number1} + {number2} is {addition}')
print(f'The result of {number1} - {number2} is {subtraction}')
print(f'The result of {number1} * {number2} is {multiplication}')
print(f'The result of {number1} / {number2} is {division}')

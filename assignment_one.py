first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the first number: '))

# perform Addition
addition = first_number + second_number

# perform subtraction
subtraction = first_number - second_number

# perform multiplication
multiplication = first_number * second_number


# perform division
if second_number != 0:
    division = first_number / second_number
else:
    division = "undefined (cannot be divided by zero)"

# print section
print(f'The result of {first_number} + {second_number} is {addition}')
print(f'The result of {first_number} - {second_number} is {subtraction}')
print(f'The result of {first_number} * {second_number} is {multiplication}')
print(f'The result of {first_number} / {second_number} is {division}')

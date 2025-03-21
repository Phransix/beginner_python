# This program calculates the sum of numbers
print('This program calculates the sum of numbers you wish to calculate.')
# Set the accumulator to zero
total = 0.0
# Get the number or user enters zero to quit [sentinel]
number = float(input('Enter a number or zero to quit: '))

# while number is not equl to zero, begin the loop process
while number != 0:
    # Add the number to the running total
    total = total + number
    # prompt the user again to enter a number or zero to quit
    number = float(input('Enter the next number or zero to quit: '))
# Print the total to the user. This must be done outside the loop
print('The sum of the numbers you entered is ', total)
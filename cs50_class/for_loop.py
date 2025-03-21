# A simple program that prints student name in a list
# for name in ['alice', 'cordelia', 'evans', 'richard', 'precious']:
#     print(name.title())

# Using range 
# for x in range(5):
#     print(str(x+1) + '. I trust God too much to give up')

# A for loop program that displays numbers and their squares
# print('Number\t\tSquare')
# print('------------------------')
# for number in range(1,12):
#     square = pow(number,2)
#     print(number, '\t\t', square)

# Calculating a running total
print('This program calculates the sum of numbers you wish to calculate.')
# Get the maxumim number the user wish to calculate for
maxNumber = int(input('How many numbers do you wish to calculate for?: '))
# Set the accumulator to zero
total = 0.0

for count in range(maxNumber):
    # prompt the user to enter a number
    number = float(input('Enter number ' + str(count + 1)+ ': '))
    # Add the number to the running total
    total = total + number
# Print the total to the user. This must be done outside the loop
print('The sum of the numbers you entered is ', total)
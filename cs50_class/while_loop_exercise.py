# A program to calculate sales person commission using the concept of loop
continue_calculation = 'y'
while continue_calculation == 'y':
    # Get a salesperson's sales and commission rate
    sales = float(input('Enter the amount of sales made: '))
    comm_rate = float(input('Enter the commission rate: '))

    # Calculate the commission
    commission = sales * (comm_rate/100)

    # Display the commission to the  user
    print('The commission is GH %.2f' %commission)

    # Ask user if he wants to perform another computations
    continue_calculation = input('Do you want to continue? ' + '(Enter y to continue):').lower()
print('Good Bye!.. See you next time.')
# calculating compound interest
def main():
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the interest rate: "))
    t = float(input("Enter the time in years: "))
    n = float(input("Enter the number of times interest is compounded per year: "))

    comp_result = compound_interest(p, r, t, n)

    print("The compound interest is %.2f" %comp_result)

def compound_interest(p, r, t, n):

    amount =  p * (1 + (r/100)/n)**(n*t)

    # Calculate the compound interest
    compound_interest = amount - p
    
    return compound_interest

main()


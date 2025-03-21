def main():
    # x = 5
    x = int(input('What\'s x: '))
    # y =6
    y = int(input('What\'s x: '))
    # z = x + y
    # print(z)
    print("Your answer is ", compute(x,y))

def compute(num1, num2):
    return num1 + num2

main()
# This is the symbol for an inline comment or a one line comment

def main():
    name = input("What is your name? ")
    formatted_name = name.strip()
    my_func(formatted_name)
    # print("Hello, " + formatted_name)
    # print("hello, ", end="")
    # print(f'Hello {formatted_name.capitalize()}')
    # print(type(name))

def my_func(name):
    print('hello, ' + name)


main()
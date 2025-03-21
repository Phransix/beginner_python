'''
Create a Python function to check if a given string is a
palindrome
'''
word = input("Enter a word: ")
if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
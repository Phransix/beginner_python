from statistics import mean
import sys

# answer = mean([2,3,456,7,4,5])
# print(answer)

# try:
#     print('My name is' , sys.argv[1])
# except IndexError:
#     print('Too few argumments')


# An alternative approach to catching the error 
# if len(sys.argv) < 2:
#     print('Few arguments')
# elif len(sys.argv) > 2:
#     print('Many arguments')
# else:
#     print('My name is' , sys.argv[1])

if len(sys.argv) < 2:
    sys.exit()
elif len(sys.argv) > 2:
    sys.exit()

print('My name is' , sys.argv[1])
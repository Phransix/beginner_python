# a = 1000
# while a != 0:
#     print(a ,':God is Great')
#     a-= 1

print('Enter any word in mind')
lucky_word = input('Enter your lucky word in mind: ')
word_length = len(lucky_word)
print(word_length)
while word_length != 0:
    print(word_length, ':' ,lucky_word)
    word_length-=1
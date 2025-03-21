from random import choice, randint, shuffle
coin = choice(["heads","tails"])
print(coin)

dups_checks = randint(1,10)
print(dups_checks)


names = ['alice', 'cordelia', 'evans', 'richard', 'precious']
shuffle(names)
# print(names)
for name in names:
    print(name)
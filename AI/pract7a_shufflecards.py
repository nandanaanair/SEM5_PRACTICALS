# import modules
import itertools, random
# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
# shuffle the cards
random.shuffle(deck)
# draw five cards
print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])

'''
Output :

You got:
6 of Spade
10 of Club
2 of Heart
10 of Spade
12 of Diamond
'''
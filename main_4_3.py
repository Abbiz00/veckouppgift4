from data_4_random_card import rand_card
from data_4_par_card import poker_hand

#print(rand_card())
#print(rand_card())

hand1 = [rand_card() for _ in range(5)]
print(hand1)
if poker_hand(hand1):
    print("Det finns ett par i handen")
else:
    print("Det finns inte ett par i handen")


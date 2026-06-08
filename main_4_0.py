from data_4_random_card import rand_card
from data_4_par_card import poker_hand

hand1 = [rand_card() for _ in range(5)]
hand2 = [rand_card() for _ in range(5)]

print(hand1)
print(hand2)

print(poker_hand(hand1))
print(poker_hand(hand2))

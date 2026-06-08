from data_4_pretty_print import pretty_print_card
from data_4_random_card import bygg_kortlek, dela_hand
from data_4_par_card import poker_hand

hand1 = dela_hand(5)
#print(hand1)
for card in hand1:
    print(pretty_print_card(card))

if poker_hand(hand1):
    print("Det finns ett par i handen")
else:
    print("Det finns inte ett par i handen")


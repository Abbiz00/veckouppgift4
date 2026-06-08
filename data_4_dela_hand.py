import random
from data_4_random_card import bygg_kortlek

def dela_hand(antal):
    kortlek = bygg_kortlek()
    if antal > len(kortlek):
        return None
    return random.sample(kortlek, antal)
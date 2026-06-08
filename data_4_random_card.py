import random

def bygg_kortlek():
    farger = ["ruter", "hjärter", "spader", "klöver"]
    kortlek = []
    for farg in farger:
        for valor in range(2, 15):
            kortlek.append([farg, valor])
    return kortlek

def dela_hand(antal):
    kortlek = bygg_kortlek()
    if antal > len(kortlek):
        return None
    return random.sample(kortlek, antal)
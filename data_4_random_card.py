import random

def rand_card():
    farger = ["ruter", "hjärter", "spader", "klöver"]
    farg = random.choice(farger)
    valor = random.randint(2, 14)
    return [farg, valor]
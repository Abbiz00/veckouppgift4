from data_3_0 import game_21
import random
cards = [random.randint(1,13) for _ in range(13)]
print(game_21(cards))
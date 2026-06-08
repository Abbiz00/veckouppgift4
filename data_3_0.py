def game_21(numbers_array):
    sum_cards = 0
    for item in numbers_array:
        sum_cards += item
        if sum_cards > 21:
            return sum_cards
    return None
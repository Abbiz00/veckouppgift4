def poker_hand(cards):
    valorer = []
    for card in cards:
        valorer.append(card[1])

    for valor in valorer:
        if valorer.count(valor) >= 2:
            return True
    return False
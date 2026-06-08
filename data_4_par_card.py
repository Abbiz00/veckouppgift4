def poker_hand(cards):
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            samma_nummer = cards[i][1] == cards[j][1]
            # print(f"kortvalör {cards[i][1]} jämförs med kortvalör {cards[j][1]}")
            if samma_nummer:
                return True
    return False
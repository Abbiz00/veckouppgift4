def pretty_print_card(card):
    valorer = {
        2: "två",   3: "tre",   4: "fyra",
        5: "fem",   6: "sex",   7: "sju",
        8: "åtta",  9: "nio",  10: "tio",
        11: "knekt", 12: "dam", 13: "kung", 14: "ess",
    }
    farg = card[0]
    valor = card[1]
    return f"{farg} {valorer[valor]}"
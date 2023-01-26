class Hand:
    def __init__(self, cards):
        self.cards = cards

    def get_value(self):
        value = 0
        aces = 0

        for card in self.cards:
            val = card.value
            if val == 1:
                aces += 1
            else:
                value += min(val, 10)
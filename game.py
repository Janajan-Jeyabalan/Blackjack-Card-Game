from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def place_bet(self):
        while True:
            bet = float(input("Place your bet: "))
            if bet > self.player.balance:
                print("You do not have sufficient funds.")
            elif bet < self.MINIMUM_BET:
                print(f"The minimum bet is ${self.MINIMUM_BET}.")
            else:
                self.bet = bet
                self.player.balance -= bet
                break

    def get_player_hit_or_stay(self):
        while True:
            hit_or_stay = input("Would you like to hit or stay? ").lower()

            if hit_or_stay in ["hit", "stay"]:
                break

            print("That is not a valid option.")

        return hit_or_stay == "hit"  # return true if player hit, false if stay
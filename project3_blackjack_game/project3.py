# Project 3: Blackjack game
import random


class Deck:
    def __init__(self):
        self.suits = ["club", "diamond", "heart", "spade"]
        self.jqk = ["J", "Q", "K"]
        self.cards = dict()
        for suit in self.suits:
            self.cards[suit + "-Ace"] = 1
            for i in range(2, 11):
                self.cards[suit + "-" + str(i)] = i
            for court_cards in self.jqk:
                self.cards[suit + "-" + court_cards] = 10
    
    def draw(self):
        return self.cards.popitem() # return a key-value pair of one card
    
    def shuffle(self):
        shuffled_cards = {}
        shuffled_keys = list(self.cards.keys())
        random.shuffle(shuffled_keys)
        for key in shuffled_keys:
            shuffled_cards[key] = self.cards[key]
        self.cards = shuffled_cards

    def __str__(self):
        return str(self.cards)


class Player:
    def __init__(self, name="dealer", balance=99999):
        self.name = name
        self.balance = balance
        self.cards = {}
        self.stop = False
        self.value = 0
        self.value_ace_11 = 0

    def hit(self, card_name, card_value):
        if self.stop:
            print("Since you stopped, you cannot take another card")
        else:
            self.cards[card_name] = card_value
            self.value += card_value
            # keep another value for 11-ace
            if card_name.endswith("Ace"):
                self.value_ace_11 += 11
            else:
                self.value_ace_11 += card_value

    def stand(self):
        self.stop = True

    def pay_bet(self, bet):
        self.balance -= bet

    def win(self, double_bet):
        self.balance += double_bet

    def lose(self, double_bet):
        self.balance -= double_bet

    def cleanup(self):
        self.cards = {}
        self.stop = False
        self.value = 0
        self.value_ace_11 = 0

    def __str__(self):
        to_print = ""
        for card in self.cards:
            card += " "
            to_print += card
        return self.name + "'s hand: " + to_print


def main():
    # create the deck with 52 cards
    deck = Deck()

    # shuffle the deck to make cards random
    deck.shuffle()

    # create dealer
    dealer = Player()

    # create player
    start_money = 1000
    player = Player(input("Name: "), start_money)
    print(player.name + " has $" + str(player.balance))

    # make a blacklist for who did not behave well
    blacklist = []

    # initialize bet
    bet = input("Bet? (0 to quit, Enter to stay at $25) ")
    if bet == "":  # user enter nothing
        bet = 25
    else:
        bet = int(bet)
        if bet < 0:
            print("invalid bet, you are kicked off and added to the balcklist")
            blacklist.append(player.name)

    # start gambling!
    while bet != 0 and player.name not in blacklist:
        # check if player has enough money to continue
        if player.balance < bet:
            print("You are broke!")
            print("Bye bye and happy become homeless!")
            break
        else:
            player.pay_bet(bet)
            print(player.name + " has $" + str(player.balance))
        # round loop:
        while True:
            print("\nBet: $" + str(bet))
            # dealer draws
            # dealer follows the rule that if her soft hand exceeds 17, she stops drawing
            # otherwise, she will draw a card beforehand player
            if not dealer.stop and dealer.value_ace_11 < 17:
                card_name, value_drawn = deck.draw()
                dealer.hit(card_name, value_drawn)
            else:
                dealer.stop = True
            print(dealer)
            print("Dealer's value: ", str(dealer.value))
            if dealer.value > 21:
                print("Dealer bust\n")
                player.win(2 * bet)
                print(player.name + " has $" + str(player.balance))
                
                # clean up value before next round:
                dealer.cleanup()
                player.cleanup()
                break

            # player draws
            # controlled by end-users
            if not player.stop:
                option = input("Move? (hit/stay): ")
                if option.lower().startswith("h"):
                    card_name, value_drawn = deck.draw()
                    player.hit(card_name, value_drawn)
                else:
                    player.stop = True
            print(player)
            print(player.name + "'s value: " + str(player.value))
            if player.value > 21:
                print(player.name + " bust\n")
                # since the player has already paid the bet before they start the game
                # they do not need to pay again
                print(player.name + " has $" + str(player.balance))

                # clean up value before next round:
                dealer.cleanup()
                player.cleanup()
                break

            # when both of dealer and player stop drawing, compare the value between them
            # when their value11 (ace counted as 11 does not exceed 21), use it; otherwise, use value
            if dealer.stop and player.stop:
                if dealer.value_ace_11 <= 21:
                    dealer.value = dealer.value_ace_11
                if player.value_ace_11 <= 21:
                    player.value = player.value_ace_11
                if player.value > dealer.value:
                    player.win(2*bet)
                    print(player.name + " wins!\n")
                else:
                    player.lose(2*bet)
                    print(dealer.name + " wins!\n")
                print(player.name + " has $" + str(player.balance))

                # clean up value before next round:
                dealer.cleanup()
                player.cleanup()
                break

        # set bet or quit after each round
        bet = input("Bet? (0 to quit, Enter to stay at $25) ")
        if bet == "":  # user enter nothing
            bet = 25
        else:
            bet = int(bet)
            if bet < 0:
                print("invalid bet, you are kicked off and added to the blacklist")
                blacklist.append(player.name)


main()
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + ' of ' +self.suit
class Deck:
    """Create a deck of 52 cards"""
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    """Shuffle the deck"""
    def shuffle(self):
        random.shuffle(self.all_cards)
    """deal the card"""
    def deal(self):
        return self.all_cards.pop()
    def __str__(self):
        deck_comp=''
        for card in self.all_cards:
            deck_comp+='\n'+card.__str__()
        return 'The deck has:'+deck_comp
class Hand:
    def __init__(self):
        self.cards=[]
        self.aces=0
        self.value=0
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.cards.extend(new_cards)
            for card in new_cards:
                self.value+=values[card.rank]
        else:
            self.cards.append(new_cards)
            self.value+=values[new_cards.rank]
            if new_cards.rank=='Ace':
                self.aces+=1

    """手牌是否达到胜利值"""
    def adjust_vaule(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1
class Chips:
    """keep track of a player's chip,betand ongoing winnings"""
    def __init__(self):
        self.total=100
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("How many chips would you like to bet?"))
        #   注意他这里穿进来的chips居然是一个类的形式
        except:
            print("your enter is not integer")
        else:
            if chips.bet>chips.total:
                print("Sorry,your bet can't exceed",chips.total)
            else:
                break
def hit(deck,hand):
    hand.add_cards(deck.deal())
    hand.adjust_vaule()
def hit_or_stand(deck,hand):
    global playing
    while True:
        h=input("please input your choice of playing T(true) or F(false)")
        if h[0].lower()=='t':
            hit(deck,hand)
        elif h[0].lower()=='f':
            print("Players stands.Dealer is playing")
            playing=False
        else:
            print("Sorry,Please try again")
            continue
        break
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)
    #The asterisk * symbol is used to print every item in a collection, and the sep='\n ' argument prints each item on a separate line.
def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()
def player_wins(chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()

def push():
    print("Dealer and Player tie! It's a push.")

playing=True
while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    # Create & shuffle the deck, deal two cards to each player
    new_deck=Deck()
    new_deck.shuffle()

    player_hand=Hand()
    player_hand.add_cards(new_deck.deal())
    player_hand.add_cards(new_deck.deal())

    dealer_hand=Hand()
    dealer_hand.add_cards(new_deck.deal())
    dealer_hand.add_cards(new_deck.deal())

    # Set up the Player's chips
    player_chips=Chips()
    # Prompt the Player for their bet
    take_bet(player_chips)
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    while playing:  # recall this variable from our hit_or_stand function
        hit_or_stand(new_deck,player_hand)
        # Prompt for Player to Hit or Stand

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value>21:
            player_busts(player_chips)
            break
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value<=21:
        while dealer_hand.value<17:
            hit(new_deck,dealer_hand)
        # Show all cards
        show_all(player_hand,dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value>21:
            dealer_busts(player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_chips)
        else:
            push()
    # Inform Player of their chips total
    print("\nPlayer's winnings stand at", player_chips.total)
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break


import random
playing=True
suits=("黑桃","红桃","梅花","方块")
ranks=('2','3','4','5','6','7','8','9','10','J','Q','K','A')
values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}
"""Create a deck of 52 cards"""
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.vaule=values[rank]
    def __str__(self):
        return self.suit + ' of '+ self.rank
class Deck:
    def __init__(self):
        self.all_crads=[]
        for suit in suits:
            for rank in ranks:
                self.all_crads.append(Card(suit,rank))
    """Shuffle the deck"""
    def shuffle(self):
        random.shuffle(self.all_crads)
    # def __str__(self):
    def deal_one(self):
        return self.all_crads.pop()
class Chips:
    def __init__(self):
        self.total=100
        self.bet=0
    def lose_chip(self):
        self.total-=self.bet
    def win_chip(self):
        self.total+=self.bet

class Hand:
    def __init__(self):
        self.hand_card=[]
        self.adjust=0
        self.value=0
    def add_card(self,newcard):
        self.hand_card.append(newcard)
        self.value+=newcard.vaule
        if newcard.rank=='A':
            self.adjust+=1
    def ace_Adjust(self):
        while self.value>21 and self.adjust:
            self.adjust-=1
            self.value-=10
"""Ask the Player for their bet"""
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("please input integer to bet"))
        except ValueError:
            print("your input not integer")
        else:
            """Make sure that the Player's bet does not exceed their available chips"""
            if chips.bet > chips.total:
                print("your bet exceed your total")
            else:
                break

"""Show only one of the Dealer's cards, the other remains hidden"""
def show_some(player,dealer):
    print("\ndealer's hand:")
    print("<hidden card>")
    print(dealer.hand_card[1])
    print("\nplayer's hand:",*player.hand_card,sep='\n')
"""Show both of the Player's cards"""
def show_all(player,dealer):
    print("\ndealer's hand:",*dealer.hand_card,sep='\n')
    print("dealer's hand vaule:",dealer.value)
    print("\nplayer's hand:",*player.hand_card,sep='\n')
    print("player's hand vaule:",player.value)

"""Ask the Player if they wish to Hit, and take another card"""
def hit_or_stand(deck,player):
    global playing
    while True:
        h=input("please input your choice of hit(h) or stand(s)")
        if h[0].lower()=='h':
            hit(deck,player)
        elif h[0].lower()=='s':
            print("Player stands.Dealer is playing")
            playing=False
        else:
            continue
        break
def hit(deck,player):
    player.add_card(deck.deal_one())
    player.ace_Adjust()

while True:
    new_deck=Deck()
    new_deck.shuffle()

    player_hand=Hand()
    player_hand.add_card(new_deck.deal_one())
    player_hand.add_card(new_deck.deal_one())

    deal_hand=Hand()
    deal_hand.add_card(new_deck.deal_one())
    deal_hand.add_card(new_deck.deal_one())

    player_chips=Chips()
    take_bet(player_chips)

    show_some(player_hand,deal_hand)
    while playing:
        hit_or_stand(new_deck,player_hand)
        show_all(player_hand,deal_hand)
        if player_hand.value>21:
            print("player_hand bust")
            break
    if player_hand.value<=21:
        while deal_hand.value<17:
            hit(new_deck,deal_hand)
            show_all(player_hand,deal_hand)
            if player_hand.value > deal_hand.value:
                print("player wins")
                player_chips.win_chip()
            elif player_hand.value < deal_hand.value:
                print("dealer wins")
                player_chips.lose_chip()
            elif deal_hand.value>21:
                print("dealer busts")
                player_chips.win_chip()
            else:
                print("push!")

    print("\nPlayer chips total:", player_chips.total)
    new_game = input("please input your choice of game y or n")
    if new_game.lower() == 'y':
        playing = True
        continue
    else:
        print("thank your playing")
        break

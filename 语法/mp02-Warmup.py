"""We will use Python OOP to simulate a simplified version of the game war. Two players will each start off with half the deck, then they each remove a card, compare which card has the highest value, and the player with the higher card wins both cards."""
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

# two_heart=Card(suits[0],ranks[0])
class Deck:

    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank))
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
# deck=Deck()
# print(len(deck.all_cards))
class Player:
    def __init__(self,name):
        self.name=name
        self.all_card=[]
    def add_cards(self,new_card):
        if type(new_card)==type([]):
            self.all_card.extend(new_card)
        else:
            self.all_card.append(new_card)
    def remove_one(self):
        return self.all_card.pop(0)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_card)} cards.'
# unni=Player('unni')
# unni.add_cards(two_heart)
# print(unni)
deck=Deck()
# new_deck=deck.shuffle() Note this doesn't return anything
deck.shuffle()
play_one=Player("one")
play_two=Player("two")
play_round=int(len(deck.all_cards)/2)
"""各自填装完毕"""
for num in range(play_round):

    play_one.add_cards(deck.deal_one())
    play_two.add_cards(deck.deal_one())
"""出牌比赛环节"""
game_on=True
round_num=0
while game_on:
    """先检查是否还有牌"""
    round_num+=1
    print(f"round{round_num}")
    if len(play_one.all_card)==0 or len(play_two.all_card)==0:
        game_on=False
        break
    """各自都出一张牌"""
    play_one_output=play_one.remove_one()
    play_two_output=play_two.remove_one()
    """对比较结果做出反应"""
    if play_two_output.value<play_one_output.value:
        play_one.add_cards(play_one_output)
        play_one.add_cards(play_two_output)
        game_on=False
        break
    elif play_two_output.value>play_one_output.value:
        play_two.add_cards(play_one_output)
        play_two.add_cards(play_two_output)
        game_on=False
        break
    else:
        continue
    print(len(play_one.all_card))
    print(len(play_two.all_card))
    print(play_one_output)
    print(play_two_output)

"""他会一直比较 因为判断条件是手牌所以会出现不会停的情况"""
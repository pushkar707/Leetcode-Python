import random

Suite = ('Hearts' , 'Spades' , 'Daimonds' , 'Clubs')
Rank = ('Ace' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten' , 'Jack' , 'Queen' , 'King')
Values = {"Ace":1 , "Two":2 , "Three":3 , "Four":4 , "Five":5 , "Six":6 , "Seven":7 , "Eight":8 , "Nine":9 , "Ten":10 , "Jack":10 , "Queen":10 , "King":10}

class Card():

    def __init__(self , rank , suite):
        self.rank = rank
        self.suite = suite
        self.value = Values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suite}"

class Deck():

    all_card = []

    def __init__(self):
        for suite in Suite:
            for rank in Rank:
                self.all_card.append(Card(rank , suite))

    def shuffle(self):
        random.shuffle(self.all_card)

    def get_one(self):
        return self.all_card.pop()

class Player():

    cards = []
    total = 0

    def hit(self , card):
        self.cards.append(card)
        

    def card_total(self):
        self.total += self.cards[-1].value
        print(f'Your total is {self.total}')

    def stay(self):
       print(f'Your total is {self.total}')

    def ace_pick(self):
        if(self.cards[-1].value == 1):
            while(True):
                ace_input = input('Press 1 or 11 to set value of your ace: ')
                if(ace_input == '1'):
                    break
                elif(ace_input == '11'):
                    self.total += 10
                    break
                else:
                    print('Enter valid number')           

class Dealer():

    cards = []
    total = 0

    def take_card(self , card):
        self.cards.append(card)

    def show_One(self):
        return self.cards[0]
    
    def cards_total(self):
        for i in range(len(self.cards)):
            self.total = self.total + self.cards[i].value
        print(f"The Second Card of dealer is {self.cards[1]}")
        print(f"`The total of dealer is {self.total}.") 
        
rules =  '''
Press B to Begin 
Press H to hit a Card.
Press S to stay
'''
print(rules)
while(True):

    player_input = input('Enter A Letter: ')

    if(player_input == 'B' or player_input == 'b'):
        deck = Deck()
        deck.shuffle()

        player = Player()
        # player.hit(deck.get_one())
        # print(f"The card you just chose is {player.cards[-1]}")
        # player.ace_pick()
        # player.hit(deck.get_one())
        # print(f"The card you just chose is {player.cards[-1]}")
        # player.ace_pick()

        dealer = Dealer()
        dealer.take_card(deck.get_one())
        dealer.take_card(deck.get_one())

        print("=====GAME STARTS=====")
        print("First Card of Dealer:\n")

        print(dealer.show_One())
        print('')

        # print('\nYour Cards:\n')
 
        # for i in range(len(player.cards)):
        #     print(player.cards[i])

        # player.total += player.cards[0].value
        # player.card_total()

    elif(player_input == 'H' or player_input == 'h'):
        player.hit(deck.get_one())
        print(f"The card you just chose is {player.cards[-1]}")
        player.ace_pick()
        player.card_total()

        if(player.total>21):
            print('The total of your cards exceeds 21. Dealer Wins.')
            exit()
        

    elif(player_input == 'S' or player_input == 's'):
        player.stay()
        dealer.cards_total()

        if(player.total > dealer.total):
            print("You win.")
            exit()
        elif(player.total < dealer.total):
            print("Dealer Wins")
            exit()
        else:
            print('Nobody won')
            exit()

    else:
        print('Please Enter A valid letter.')
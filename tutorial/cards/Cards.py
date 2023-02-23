import random
class Card:
    suits = (None, "spades", "clubs", "diamonds", "hearts")
    values = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace")

    def __init__(self, s, v):
        self.suit = s
        self.value = v

    def __repr__(self):
        result =""
        su = self.suits[self.suit]
        result = str(self.value) + " of " + su
        return result

        
    
    def __lt__(self, c2):
        if(self.value < c2.value):
            return True
        elif(self.value == c2.value):
            if self.suit < c2.suit:
                return True
            else:
                return False
        else:
            return False
    
    def __gt__(self, c2):
        if(self.value > c2.value):
            return True
        elif(self.value == c2.value):
            if self.suit > c2.suit:
                return True
            else:
                return False
        else:
            return False

class Deck:
    def __init__(self):
        self.cards = []
        for value in range(2, 15):
            for suit in range(1, 5):
                self.cards.append(Card(suit, value))
        random.shuffle(self.cards)
    
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name =  name

class Game:
    def __init__(self):
        name1 = input("enter player1 desired name: ")
        self.player1 = Player(name1)
        name2 = input("enter player2 desired name: ")
        self.player2 = Player(name2)
        self.deck = Deck()

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew a {}\n{} drew a {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)
    
    def wins(self, player):
        w = "{} wins this round!"
        w = w.format(player)
        print(w)

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p2.wins > p1.wins:
            return p2.name
        return 0

    def play_game(self):
        cards = self.deck.cards
        print("WAR DECLARED")
        while len(cards) >= 2:
            m = "q to Quit, any key to play "
            response = input(m)
            if(response == "q"):
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.player1.name
            p2n = self.player2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.player1.wins += 1
                self.wins(self.player1.name)
            else:
                self.player2.wins += 1
                self.wins(self.player2.name) 

        winner = self.winner(self.player1, self.player2)
        if winner != 0:
            print("{} has won the war!!".format(winner))
        else:
            print("tie")

game1 = Game()
game1.play_game()
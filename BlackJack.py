# Mini-project #6 - Blackjack
import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
GAP = 20
OFFSET = 50
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
flag = True
outcome = ""
messages = "Hit or stand?"
score = [0, 0]
hand_value = [0, 0]

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []  # create Hand object
        self.st = ''
        self.net_value = None

    def __str__(self):
        s = 'Cards in hand are: ' + self.st
        return s  # return a string representation of a hand
    
    def draw_cards(self, canvas, pos):
        card_count = 0
        for card in self.cards:
            dynamic_pos = [(1+card_count)*pos[0], pos[1]]
            card.draw(canvas, dynamic_pos)
            card_count += 1
            
    def add_card(self, card):
        self.cards.append(card)
        self.st = self.st + card.suit + card.rank + ' '

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        self.net_value = 0
        A_count = 0
        for card in self.cards:
            if card.rank == 'A':
                self.net_value += 11
                A_count += 1
            elif card.rank != 'A':
                self.net_value += VALUES[card.rank]
        while self.net_value > 21 and A_count >= 1:
            self.net_value -= 10
            A_count -= 1
        return self.net_value
    
# define deck class 
class Deck:
    def __init__(self):
        self.Deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.Deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.Deck)

    def deal_card(self):
        return self.Deck.pop()  # deal a card object from the deck

    def __str__(self):
        st = ''
        for card in self.Deck:
            st = st + card.suit + card.rank + ' '
        return 'Deck consists of ' + st  # return a string representing the deck


h1 = Hand()
h2 = Hand() 
d1 = Deck()
d2 = Deck()

def new_game():
    global outcome
    outcome = ''
    h1.cards = []
    h2.cards = []
    hand_value[0] = 0
    hand_value[1] = 0

def evaluate():
    global outcome, score, in_play, flag
    if hand_value[0] > 21:
        outcome = "Sorry, but you're #busted"
        score[1] += 1
    elif hand_value[1] > 21:
        outcome = "Dealer's busted, Corngrass!"
        score[0] += 1
    else:
        if hand_value[0] > hand_value[1]:
            if hand_value[0] - hand_value[1] <= 2:
                outcome = "You win, come on!"
            else:
                outcome = "You win, Corngrass!"
            score[0] += 1
        else:
            if hand_value[1] - hand_value[0] <= 2:
                outcome = "Dealer wins, hard luck :("
            else:
                outcome = "Dealer has won"
            score[1] += 1
    in_play = False
    print 'Score: ', score, '\n', 'Outcome : ', outcome, '\n'


#define event handlers for buttons
def deal():
    global outcome, in_play, flag, outcome, messages
    if(in_play == True):
        outcome = "You lost because of re-deal!"
        messages = "New deal?"
        score[1] += 1
        in_play = False
        flag = False
    else:
        new_game()
        d1.shuffle()
        d2.shuffle()
        for _ in range(2):
            c1 = d1.deal_card()
            c2 = d2.deal_card()
            h1.add_card(c1)
            h2.add_card(c2)
            hand_value[0] = h1.get_value()
            hand_value[1] = h2.get_value()
            print c1, c2
            print hand_value[0], hand_value[1]
        in_play = True
        flag = True
        messages = "Hit or stand?"

def hit():
    global outcome, in_play, messages # replace with your code below
 
    # if the hand is in play, hit the player
    if in_play:
        messages = 'Player hits!'
        print in_play
        d1.shuffle()
        c1 = d1.deal_card()
        h1.add_card(c1)
        hand_value[0] = h1.get_value()
        print c1, ' -'
        print hand_value[0], hand_value[1]
        # if busted, assign a message to outcome, update in_play and score
        if hand_value[0] > 21:
            evaluate()
    
def stand():
    global score, in_play, messages # replace with your code below
    if in_play:
        messages = "Who's winning this!? New Deal?"
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while hand_value[1] < 17:
            d2.shuffle()
            c2 = d2.deal_card()
            print '- ', c2
            h2.add_card(c2)
            hand_value[1] = h2.get_value()
            print hand_value[0], hand_value[1]
        # assign a message to outcome, update in_play and score
        evaluate()
    
# draw handler    
def draw(canvas):
    # all timers
    canvas.draw_text('BLACKJACK', (185, 60), 50, 'Purple')
    canvas.draw_text('Dealer Score : ' + str(score[1]), (350, 200), 25, 'Green')
    canvas.draw_text('Your Score : ' + str(score[0]), (350, 450), 25, 'Yellow')
    h1.draw_cards(canvas, [(CARD_SIZE[0] + GAP), 475])
    h2.draw_cards(canvas, [(CARD_SIZE[0] + GAP), 225])
    # in_play candidates only
    if in_play is False and flag is False:
        canvas.draw_text(messages, (75, 135), 25, 'White')
        canvas.draw_text(outcome, (100, 380), 35, 'Red')
    elif in_play is True and flag is True:
        canvas.draw_text(messages, (75, 135), 25, 'White')
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [CARD_CENTER[0] + (CARD_SIZE[0] + GAP), CARD_CENTER[1] + 225], CARD_BACK_SIZE)
    # not_  in_play candidates only
    elif in_play is False and flag is True:
        canvas.draw_text(messages, (75, 135), 25, 'White')
        canvas.draw_text('Value : ' + str(hand_value[1]), (100, 200), 25, 'Blue')
        canvas.draw_text('Value : ' + str(hand_value[0]), (100, 450), 25, 'Blue')
        canvas.draw_text(outcome, (100, 380), 35, 'Red')
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Black")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
new_game()
deal()
frame.start()


# remember to review the gradic rubric
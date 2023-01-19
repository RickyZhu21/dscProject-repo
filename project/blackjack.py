from deck import Deck
from hand import DealerHand, PlayerHand
from card import Card

# don't change these imports
from numpy.random import randint, seed
seed(20)

class Blackjack:
    """
    Game of blackjack!

    # Removes the game summaries from the previous doctest run
    >>> from os import remove, listdir
    >>> for f in listdir("game_summaries"):
    ...    remove("game_summaries/" + f)

    #######################################
    ### Doctests for calculate_score() ####
    #######################################
    >>> card_1 = Card("A", "diamonds")
    >>> card_2 = Card("J", "spades")
    >>> hand_1 = PlayerHand()
    >>> Blackjack.calculate_score(hand_1)
    0
    >>> hand_1.add_card(card_1)
    >>> Blackjack.calculate_score(hand_1) # (Ace)
    11
    >>> hand_1.add_card(card_2)
    >>> Blackjack.calculate_score(hand_1) # (Ace, Jack)
    21

    >>> card_3 = Card("A", "spades")
    >>> hand_2 = PlayerHand()
    >>> hand_2.add_card(card_1, card_3)
    >>> Blackjack.calculate_score(hand_2) # (Ace, Ace)
    12
    >>> hand_2.add_card(card_2)
    >>> Blackjack.calculate_score(hand_2) # (Ace, Ace, Jack)
    12

    >>> hand_3 = PlayerHand()
    >>> card_4 = Card(2, "spades")
    >>> card_5 = Card(4, "spades")
    >>> hand_3.add_card(card_4, card_5)
    >>> Blackjack.calculate_score(hand_3)
    6

    #######################################
    ### Doctests for determine_winner() ####
    #######################################
    >>> blackjack = Blackjack(10)
    >>> blackjack.determine_winner(10, 12)
    -1
    >>> blackjack.determine_winner(21, 21)
    0
    >>> blackjack.determine_winner(22, 23)
    0
    >>> blackjack.determine_winner(12, 2)
    1
    >>> blackjack.determine_winner(22, 2)
    -1
    >>> blackjack.determine_winner(2, 22)
    1
    >>> print(blackjack.get_log())
    Player lost with a score of 10. Dealer won with a score of 12.
    Player and Dealer tie.
    Player and Dealer tie.
    Player won with a score of 12. Dealer lost with a score of 2.
    Player lost with a score of 22. Dealer won with a score of 2.
    Player won with a score of 2. Dealer lost with a score of 22.
    <BLANKLINE>  
    >>> blackjack.reset_log()

    #######################################
    ### Doctests for play_round() #########
    #######################################
    >>> blackjack_2 = Blackjack(10)
    >>> blackjack_2.play_round(1, 15)
    >>> print(blackjack_2.get_log())
    Round 1 of Blackjack!
    wallet: 10
    bet: 5
    Player Cards: (10, spades) (A, spades)
    Dealer Cards: (Q, spades) (?, ?)
    Dealer Cards Revealed: (7, hearts) (Q, spades)
    Player won with a score of 21. Dealer lost with a score of 17.
    <BLANKLINE>
    
    >>> blackjack_2.reset_log()
   
    >>> blackjack_2.play_round(3, 21)
    >>> print(blackjack_2.get_log())
    Round 2 of Blackjack!
    wallet: 15
    bet: 5
    Player Cards: (4, spades) (7, spades)
    Dealer Cards: (A, diamonds) (?, ?)
    (J, diamonds) was pulled by a Player
    Dealer Cards Revealed: (5, spades) (A, diamonds)
    (6, spades) was pulled by a Dealer
    (2, spades) was pulled by a Dealer
    (8, spades) was pulled by a Dealer
    Player won with a score of 21. Dealer lost with a score of 22.
    Round 3 of Blackjack!
    wallet: 20
    bet: 10
    Player Cards: (6, diamonds) (9, hearts)
    Dealer Cards: (K, diamonds) (?, ?)
    (Q, diamonds) was pulled by a Player
    Dealer Cards Revealed: (J, hearts) (K, diamonds)
    Player lost with a score of 25. Dealer won with a score of 20.
    Round 4 of Blackjack!
    wallet: 10
    bet: 5
    Player Cards: (5, hearts) (10, hearts)
    Dealer Cards: (2, hearts) (?, ?)
    (3, hearts) was pulled by a Player
    (7, clubs) was pulled by a Player
    Dealer Cards Revealed: (2, hearts) (2, diamonds)
    (K, clubs) was pulled by a Dealer
    (3, clubs) was pulled by a Dealer
    Player lost with a score of 25. Dealer won with a score of 17.
    <BLANKLINE>
    
    >>> with open("game_summaries/game_summary2.txt", encoding = 'utf-8') as f:
    ...     lines = f.readlines()
    ...     print("".join(lines[10:26]))
    Dealer Hand:
    ____
    |7  |
    | ♥ |
    |__7|
    ____
    |Q  |
    | ♠ |
    |__Q|
    Winner of ROUND 1: Player
    <BLANKLINE>
    ROUND 2:
    Player Hand:
    ____
    |4  |
    | ♠ |
    <BLANKLINE>

    >>> blackjack_3 = Blackjack(5)
    >>> blackjack_3.play_round(5, 21)
    >>> print(blackjack_3.get_log())
    Round 1 of Blackjack!
    wallet: 5
    bet: 5
    Player Cards: (2, spades) (2, diamonds)
    Dealer Cards: (2, hearts) (?, ?)
    (3, spades) was pulled by a Player
    (3, hearts) was pulled by a Player
    (3, diamonds) was pulled by a Player
    (3, clubs) was pulled by a Player
    (4, spades) was pulled by a Player
    (4, hearts) was pulled by a Player
    Dealer Cards Revealed: (2, hearts) (2, clubs)
    (4, diamonds) was pulled by a Dealer
    (4, clubs) was pulled by a Dealer
    (5, spades) was pulled by a Dealer
    Player lost with a score of 24. Dealer won with a score of 17.
    Wallet amount $0 is less than bet amount $5.

    >>> blackjack_4 = Blackjack(500)
    >>> blackjack_4.play_round(13, 21) # At least 52 cards will be dealt
    >>> blackjack_4.reset_log()
    >>> blackjack_4.play_round(1, 17)
    >>> print(blackjack_4.get_log())
    Not enough cards for a game.
    """
    # Class Attribute(s)
    num_games = 1

    def __init__(self, wallet):
        # Initialize instance attributes
        # auto-increment as needed
        assert isinstance(wallet, int) or isinstance(wallet, float)
        self.deck = Deck()
        self.wallet = wallet
        Blackjack.num_games += 1
        self.game_number = Blackjack.num_games
        self.log = ""
        self.bet = 5
        self.round_num = 0
    
    def play_round(self, num_rounds, stand_threshold):
        """
        Plays `num_rounds` Blackjack rounds.

        Parameters:
            num_rounds (int): Number of rounds to play.
            stand_threshold (int): Score threshold for when the player
            will stand (ie player stands if they have a score >= 
            this threshold)
        """
        # This could get pretty long!
        play = True
        self.bet = 5
        while play == True:
            for i in range(num_rounds):
                if len(self.deck.get_cards()) < 4:
                    self.log += "Not enough cards for a game."
                    play = False
                    break
                if self.bet > self.wallet:
                    self.log += "Wallet amount ${} is less than bet amount ${}."\
                    .format(self.wallet, self.bet)
                    play = False
                    break
                self.round_num += 1
                self.log += "Round {} of Blackjack!\n".format(self.round_num)
                self.log += "wallet: " + str(self.wallet) + "\n"
                self.log += "bet: " + str(self.bet) + "\n"
                mongean_shuffle = randint(6)
                modified_overhand_shuffle = randint(6)
                self.deck.shuffle(modified_overhand = modified_overhand_shuffle, \
                                  mongean = mongean_shuffle)
                #print(self.deck.get_cards())
                player = PlayerHand()
                dealer = DealerHand()
                self.deck.deal_hand(player)
                self.deck.deal_hand(dealer)
                self.deck.deal_hand(player)
                self.deck.deal_hand(dealer)
                self.log += "Player Cards: {} {}\n".format(player.get_cards()[0].__repr__(), \
                                                           player.get_cards()[1].__repr__())
                self.log += "Dealer Cards: {} {}\n".format(dealer.get_cards()[0].__repr__(), \
                                                           dealer.get_cards()[1].__repr__())
                self.hit_or_stand(player, stand_threshold)
                dealer.reveal_hand()
                self.log += "Dealer Cards Revealed: {}\n".format(dealer.__repr__())
                #dealer.sort_hand()
                #if (Card.__lt__(dealer.get_cards()[1], dealer.get_cards()[0]))== True:
                #    self.log += "Dealer Cards Revealed: {} {}\n".format(dealer.get_cards()[0].__repr__(), dealer.get_cards()[1].__repr__())
                #if (Card.__lt__(dealer.get_cards()[0], dealer.get_cards()[1]))== True:
                #    self.log += "Dealer Cards Revealed: {} {}\n".format(dealer.get_cards()[1].__repr__(), dealer.get_cards()[0].__repr__())
                dealer_stand_threshold = 17
                self.hit_or_stand(dealer, dealer_stand_threshold)
                #print(Blackjack.calculate_score(player))
                #print(self.determine_winner((Blackjack.calculate_score(player)), (Blackjack.calculate_score(dealer))))
                win = self.determine_winner((Blackjack.calculate_score(player)), (Blackjack.calculate_score(dealer)))
                if win == 1:
                    self.wallet += self.bet
                    self.bet += 5
                if win == -1:
                    self.wallet -= self.bet
                    self.bet -= 5
                play = False
                self.add_to_file(player, dealer)
            
    def calculate_score(hand):
        """
        Calculates the score of a given hand. 

        Sums up the ranks of each card in a hand. Jacks, Queens, and Kings
        have a value of 10 and Aces have a value of 1 or 11. The value of each
        Ace card is dependent on which value would bring the score closer
        (but not over) 21. 

        Should be solved using list comprehension and map/filter. No explicit
        for loops.

        Parameters:
            hand: The hand to calculate the score of.
        Returns:
            The best score as an integer value.
        """
        cards = [card.get_rank() for card in hand.cards]
        ace_count = cards.count("A")
        rank_modified1 = list(map(lambda x: 10 if x in ["J", "Q", "K"] else x, cards))
        rank_modified2 = list(map(lambda x: 11 if x == "A" else x, rank_modified1))
        total = sum(rank_modified2)
        if total > 21 and ace_count > 0:
            total = total - 10
        if total > 21 and ace_count > 1:
            total = total - 10
        if total > 21 and ace_count > 2:
            total = total - 10
        if total > 21 and ace_count > 3:
            total = total - 10
        return total
    def determine_winner(self, player_score, dealer_score):
        """
        Determine whether the Blackjack round ended with a tie, dealer winning, 
        or player winning. Update the log to include the winner and
        their scores before returning.

        Returns:
            1 if the player won, 0 if it is a tie, and -1 if the dealer won
        """
        if player_score > 21 and dealer_score <= 21:
            self.log += "Player lost with a score of "+ str(player_score)+". Dealer won with a score of "+str(dealer_score)+".\n"
            return -1
        elif player_score <= 21 and dealer_score <= 21:
            if player_score > dealer_score:
                self.log += "Player won with a score of "+ str(player_score)+". Dealer lost with a score of "+str(dealer_score)+".\n"
                return 1
            elif player_score < dealer_score:
                self.log += "Player lost with a score of "+ str(player_score)+". Dealer won with a score of "+str(dealer_score)+".\n"
                return -1
            elif player_score == dealer_score:
                self.log += 'Player and Dealer tie.\n'
                return 0
        elif player_score > 21 and dealer_score > 21:
            self.log += 'Player and Dealer tie.\n'
            return 0
        elif player_score <= 21 and dealer_score > 21:
            self.log += "Player won with a score of "+ str(player_score)+". Dealer lost with a score of "+str(dealer_score)+".\n"
            return 1
    def hit_or_stand(self, hand, stand_threshold):
        """
        Deals cards to hand until the hand score has reached or surpassed
        the `stand_threshold`. Updates the log everytime a card is pulled.

        Parameters:
            hand: The hand the deal the cards to depending on its score.
            stand_threshold: Score threshold for when the player
            will stand (ie player stands if they have a score >= 
            this threshold).
        """
        while Blackjack.calculate_score(hand) < stand_threshold and len(self.deck.get_cards()) > 0:
            if isinstance(hand, DealerHand):
                self.log +="{} was pulled by a Dealer\n".format(self.deck.get_cards()[0].__repr__())
                self.deck.deal_hand(hand)
            elif isinstance(hand, PlayerHand):
                self.log += "{} was pulled by a Player\n".format(self.deck.get_cards()[0].__repr__())
                self.deck.deal_hand(hand)

    def get_log(self):
        return self.log
    def reset_log(self):
        self.log = ""
    def add_to_file(self, player_hand, dealer_hand, result):
        """
        Writes the summary and outcome of a round of Blackjack to the 
        corresponding .txt file. This file should be named game_summaryX.txt 
        where X is the game number and it should be in `game_summaries` 
        directory.
        """
        
        # Remember to use encoding = "utf-8" 
        with open("game_summaries/game_summary" + str(self.game_number) +".txt", 'w',\
        encoding = "utf-8") as f:
            for round in range(self.round_play):
                f.write("ROUND " + str(round) + ":\n")
                f.write("Player Hand:\n")
                f.write(player_hand.__str__() + "\n")
                f.write("Dealer Hand:\n")
                f.write(dealer_hand.__str__() + "\n")
                #So should be 1, -1, 0 for winning, losing, or tie. 
                if result == 1:
                    f.write("Winner of ROUND " + str(round) + ":" + "Player\n")
                if result == 0:
                    f.write("Winner of ROUND " + str(round) + ":" + "Tied\n")
                if result == -1:
                    f.write("Winner of ROUND " + str(round) + ":" + "Dealer\n")
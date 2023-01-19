class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    >>> card_4 = Card(10, "spades")
    >>> print(card_4)
    ____
    |10  |
    | ♠ |
    |__10|

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    True

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        assert rank in ["A", "J", "Q", "K"] or rank in range(2, 11)
        assert suit in ["hearts", "spades", "clubs", "diamonds"]
        assert isinstance(visible, bool)
        self.rank = rank
        self.suit = suit
        self.visible = visible
        

    def __lt__(self, other_card):
        if self.rank != other_card.rank:
            if self.rank == "J" and other_card.rank in ["Q", "K", "A"]:
                return True
            elif self.rank in ["Q", "K", "A"] and other_card.rank == "J":
                return False
            elif self.rank == "Q" and other_card.rank in ["K", "A"]:
                return True
            elif self.rank in ["K", "A"] and other_card.rank == "Q":
                return False
            elif self.rank == "K" and other_card.rank == "A":
                return True
            elif self.rank == "A" and other_card.rank == "K" :
                return False
            elif other_card.rank == "A":
                return True
            elif self.rank == "A":
                return False
            elif self.rank in ["A", "J", "Q", "K"] and isinstance(other_card.rank, int):
                return False
            elif isinstance(self.rank, int) and other_card.rank in ["A", "J", "Q", "K"]:
                return True
            elif isinstance(self.rank, int) and isinstance(other_card.rank, int):
                if self.rank < other_card.rank:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if self.suit == "clubs" and other_card.suit != "clubs":
                return False
            elif other_card.suit == "clubs" and self.suit != "clubs":
                return True
            elif self.suit == "diamonds" and other_card.suit in ["hearts", "spades"]:
                return False
            elif self.suit in ["hearts", "spades"] and other_card.suit == "diamonds":
                return True
            elif self.suit == "hearts" and other_card.suit == "spades":
                return False
            elif self.suit == "spades" and other_card.suit == "hearts":
                return True
            else:
                return False





    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        if self.visible == True and isinstance(self.rank, str) == True:
            if self.suit == "hearts":
                return "____\n" + "|" + self.rank + "  |\n" + "| ♥ |\n" +\
                "|__" + self.rank + "|"
            elif self.suit == "spades":
                return "____\n" + "|" + self.rank + "  |\n" + "| ♠ |\n" +\
                "|__" + self.rank + "|"
            elif self.suit == "clubs":
                return "____\n" + "|" + self.rank + "  |\n" + "| ♣ |\n" +\
                "|__" + self.rank + "|"
            elif self.suit == "diamonds":
                return "____\n" + "|" + self.rank + "  |\n" + "| ♦ |\n" +\
                "|__" + self.rank + "|"
        elif self.visible == True and isinstance(self.rank, int) == True:
            if self.suit == "hearts":
                return "____\n" + "|" + str(self.rank) + "  |\n" + "| ♥ |\n" +\
                "|__" + str(self.rank) + "|"
            elif self.suit == "spades":
                return "____\n" + "|" + str(self.rank) + "  |\n" + "| ♠ |\n" +\
                "|__" + str(self.rank) + "|"
            elif self.suit == "clubs":
                return "____\n" + "|" + str(self.rank) + "  |\n" + "| ♣ |\n" +\
                "|__" + str(self.rank) + "|"
            elif self.suit == "diamonds":
                return "____\n" + "|" + str(self.rank) + "  |\n" + "| ♦ |\n" +\
                "|__" + str(self.rank) + "|"
        else:
            return "____\n" + "|" + "?" + "  |\n" + "| ? |\n" +\
                "|__" + "?" + "|"



    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """
        if self.visible == True and isinstance(self.get_rank(), str) == True:        
            return "(" + self.get_rank() + ", " + self.get_suit() + ")"
        elif self.visible == True and isinstance(self.get_rank(), int) == True:
            return "(" + str(self.get_rank())+ ", " + self.get_suit() + ")"   
        else:
            return "(" + "?" + ", " + "?" + ")"
    
    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit 

    def set_visible(self, visible):
        assert isinstance(visible, bool)
        self.visible = visible

    
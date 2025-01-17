from card import Card

class PlayerHand():
    """
    >>> card_1 = Card("A", "spades")
    >>> card_2 = Card(2, "diamonds")
    >>> card_3 = Card(3, "clubs")
    >>> card_4 = Card(4, "hearts")
    >>> card_5 = Card(5, "spades")
    >>> card_6 = Card("K", "diamonds")
    >>> card_7 = Card("J", "clubs")
    >>> card_8 = Card("Q", "hearts")
    
    >>> p_hand = PlayerHand()
    >>> p_hand.add_card(card_1, card_2)
    >>> p_hand
    (2, diamonds) (A, spades)
    >>> p_hand.add_card(card_3)
    >>> print(p_hand)
    ____
    |2  |
    | ♦ |
    |__2|
    ____
    |3  |
    | ♣ |
    |__3|
    ____
    |A  |
    | ♠ |
    |__A|
    
    >>> p_hand
    (2, diamonds) (3, clubs) (A, spades)

    >>> d_hand = DealerHand()
    >>> d_hand.add_card(card_4)
    >>> d_hand.add_card(card_5, card_6)
    >>> print(d_hand)
    ____
    |4  |
    | ♥ |
    |__4|
    ____
    |?  |
    | ? |
    |__?|
    ____
    |?  |
    | ? |
    |__?|
    >>> d_hand
    (4, hearts) (?, ?) (?, ?)
    >>> d_hand.reveal_hand()
    >>> print(d_hand)
    ____
    |4  |
    | ♥ |
    |__4|
    ____
    |5  |
    | ♠ |
    |__5|
    ____
    |K  |
    | ♦ |
    |__K|
    >>> d_hand
    (4, hearts) (5, spades) (K, diamonds)
    """
    
    def __init__(self):
        self.cards = []
        
    def add_card(self, *cards):
        """
        Adds cards to the hand, then sorts
        them in ascending order.
        """
        assert all([isinstance(card, Card) for card in cards])
        for card in cards:
            self.cards.append(card)
        self.sort_hand()

    def get_cards(self):
        return self.cards           

    def __str__(self):
        """
        Returns the string representation of all cards
        in the hand, with each card on a new line.
        """
        result_str = ""
        for card in self.cards:
            result_str += card.__str__() + "\n"
        return result_str[:-1]
    
    def __repr__(self):
        """
        Returns the representation of all cards, with 
        each card separated by a space.
        """
        result_tup = ""
        for card in self.cards:
            result_tup += card.__repr__() + " "
        return result_tup[:-1]

    def sort_hand(self):
        """
        Sorts the cards in ascending order.
        """
        self.cards.sort()
        
    
class DealerHand(PlayerHand):
    
    def __init__(self):
        # This should inherit attributes from
        # the parent PlayerHand class.
        super().__init__()
        self.hand_visible = False

    def add_card(self, *cards):
        """
        Adds the cards to hand such that only the first card
        in the hand is visible (when the dealer's hand is not visible).
        If the dealer's hand is visible, then add cards to hand as 
        usual and sort them in ascending order.
        """
        assert all([isinstance(card, Card) for card in cards])
        if self.hand_visible == False:
            if len(self.cards) == 0:
                self.cards.append(cards[0])
                for i in range(1, len(cards)):
                    cards[i].set_visible(False)
                    self.cards.append(cards[i])
            else:
                for card in cards:
                    card.set_visible(False)
                    self.cards.append(card)
                # for card in cards:
                #     card.set_visible(False)
                #     self.cards.append(card) 
        else:
            for card in self.cards:
                card.__add__()
                



    
    def reveal_hand(self):
        """
        Makes all the cards in the hand visible
        and sorts them in ascending order.
        """
        self.hand_visible = True
        for card in self.cards:
            card.set_visible(True)
        self.sort_hand()

    
    
    
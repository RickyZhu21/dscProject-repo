from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, spades), (2, hearts), (2, diamonds), (2, clubs), (3, spades)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, spades), (Q, spades), (10, spades), (7, hearts), (5, hearts)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, spades)
    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        # dict = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10, "J":11, "Q":12, "K":13, "A":14}
        self.cards = sorted([Card(rank, suit) for rank in [2,3,4,5,6,7,8,9,10,"J","Q","K","A"] for suit in \
        ["spades", "hearts", "diamonds", "clubs"]])

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        assert all([isinstance(key, str) for key in shuffle_and_count.keys()])
        assert all([isinstance(value, int) for value in shuffle_and_count.values()])
        if "modified_overhand" in shuffle_and_count:
            self.cards = Shuffle.modified_overhand(self.cards, shuffle_and_count.get("modified_overhand"))
        if "mongean" in shuffle_and_count:
            for i in range(shuffle_and_count.get("mongean")):
                self.cards = Shuffle.mongean(self.cards)


    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert isinstance(hand, PlayerHand) or isinstance(hand, DealerHand)
        hand.add_card(self.cards[0])
        self.cards = self.cards[1:]

    def get_cards(self):
        return self.cards

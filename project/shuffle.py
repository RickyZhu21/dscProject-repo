class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    
    >>> odd_cards = [1, 2, 3, 4, 5]
    >>> mod_oh_even = Shuffle.modified_overhand(odd_cards, 2)
    >>> mod_oh_even
    [1, 2, 3, 4, 5]

    >>> even_cards = [0, 1, 2, 3, 4, 5]
    >>> mod_oh_odd = Shuffle.modified_overhand(even_cards, 1)
    >>> mod_oh_odd
    [2, 0, 1, 3, 4, 5]

    >>> even2_cards = [1, 2, 3, 4, 5, 6]
    >>> mod_oh_odd2 = Shuffle.modified_overhand(even2_cards, 3)
    >>> mod_oh_odd2
    [2, 4, 1, 3, 5, 6]
    """     
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """


        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        assert isinstance(cards, list)
        assert isinstance(num, int)
        assert num <= len(cards)
        if num == 0:
            return cards
        #For both odd
        if len(cards) % 2 == 1 and num % 2 == 1:
            #Start index: (len(cards))//2 - (num//2)
            #End index: ((len(cards))//2 + (num//2)) + 1
            #Then adds cards[before the start index] and cards[after the end index]
            cards_m = cards[(len(cards))//2 - (num//2) : ((len(cards))//2 + (num//2)) + 1] +\
            cards[:(len(cards))//2 - (num//2)] + cards[((len(cards))//2 + (num//2)) + 1:]
            return Shuffle.modified_overhand(cards_m, num-1)
        #for both even
        if len(cards) % 2 == 0 and num % 2 == 0:
            #Start index: (len(cards))//2 - (num//2)
            #End index: ((len(cards))//2 + (num//2))
            #Then adds cards[before the start index] and cards[after the end index]
            cards_m = cards[(len(cards))//2 - (num//2) : ((len(cards))//2 + (num//2))] +\
            cards[:(len(cards))//2 - (num//2)] + cards[((len(cards))//2 + (num//2)):]
            return Shuffle.modified_overhand(cards_m, num-1)
        #for even cards, odd num
        if len(cards) % 2 == 0 and num % 2 == 1:
            #Middle(num - 1) + last card of top half
            #Use even and even when num-1, to get the middle
            #Use the (start index of middle) - 1 to get the extra card
            #Then adds the cards(middle, even) and cards[after end index]
            cards_m = [cards[(len(cards))//2 - ((num-1)//2) - 1]] +\
            cards[(len(cards))//2 - ((num-1)//2) : ((len(cards))//2 + ((num-1)//2))] +\
            cards[:(len(cards))//2 - ((num-1)//2) - 1] + cards[((len(cards))//2 + ((num-1)//2)):]
            return Shuffle.modified_overhand(cards_m, num-1)
        if len(cards) % 2 == 1 and num % 2 == 0:
            #Middle(num - 1) + last card of top half
            #Use odd and odd when num-1, to get the middle
            #Use the (start index of middle) - 1 to get the extra card
            #Then adds the cards(middle, odd) and cards[after end index]
            cards_m = [cards[(len(cards))//2 - ((num-1)//2) - 1]] +\
            cards[(len(cards))//2 - ((num-1)//2) : ((len(cards))//2 + ((num-1)//2)) + 1] +\
            cards[:(len(cards))//2 - ((num-1)//2) - 1] + cards[((len(cards))//2 + ((num-1)//2)) + 1:]
            return Shuffle.modified_overhand(cards_m, num-1)
                    
    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        mongean_card = []
        len_cards = len(cards)
        def inner(cards1):
            if len(cards1) == 0:
                return mongean_card
            elif (len_cards - len(cards1)) % 2 == 0:
                mongean_card.append(cards1[0])
                return inner(cards1[1:])
            elif (len_cards - len(cards1)) % 2 == 1:
                mongean_card.insert(0, cards1[0])
                return inner(cards1[1:])
        return inner(cards)
    
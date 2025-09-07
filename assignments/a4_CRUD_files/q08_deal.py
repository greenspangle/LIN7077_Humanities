from typing import List, Tuple


def deal(an_int: int) -> List[Tuple[str]]:
    """This function simulates dealing `an_int` number of cards from a shuffled
    deck of playing cards. The parameter `an_int` is guaranteed to be an
    integer between 0 and 52 inclusive with a default value of one.

    A set of playing cards consists of 52 individual cards each marked as
    belonging to one of four suits (clubs, diamonds, hearts, spades) and one of
    thirteen face values (ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, knave, queen, king).
    The pack contains no duplicates so every card is unique with its deck.

    When called, this function should return a list of `an_int` playing cards
    with each card being a tuple containing two strings. The first for its face
    value and the second for its suit.

    Just like a real deck of cards, the same card cannot be dealt twice on a
    single call of `deal()`."""
    # import the random library
    import random
    # create the deck of cards
    suits = 'clubs diamonds hearts spades'.split(' ')
    faces = ('ace 2 3 4 5 6 7 8 9 10'
             ' knave queen king').split(' ')
    deck_as_list_of_tuples = []
    for s in suits:
        for f in faces:
            deck_as_list_of_tuples.append((f, s))
    # deck created as tuple for each card

    # now deal the hand
    hand_as_tuples = random.sample(deck_as_list_of_tuples, an_int)
    return hand_as_tuples

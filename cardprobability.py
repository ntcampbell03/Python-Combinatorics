'''
Prints the probability of selecting a card from a deck of 52 cards within the given rank and suit parameters

Parameters:
    rank_list: A list of all card ranks that the selected card must be within
    suit_list: A list of all card suits that the selected card must be within
'''
class Probability:
    def CardProbability(rank_list, suit_list):
        probability = len(rank_list) * 4 + len(suit_list) * 13 - len(rank_list) * len(suit_list)
        print(str(probability) + '/52,', str(probability * 100 / 52) + "%")

'''
Solves the following problem: given a certain number of people each with a specified number of friends, is there a way to arrange them
around a circular table such that no one sits next to a friend? (Makes use of Dirac's Thoerem)

Parameters:
    friends: a dictionary representing how many friends each person has
    eg. {1:2, 2:2, 3:1} means people 1 and 2 have 2 friends, and person 3 has 1 friend.
'''
class SeatingArrangements:
    def Checker(friends):
        if max(list(friends.values())) <= len(friends.keys()) // 2:
            return True
        else:
            return False

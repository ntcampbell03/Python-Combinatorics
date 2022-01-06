'''
Finds and prints the number of integer solutions to a given equation of the format a + b + c + ... = target.

Parameters:
    range_list: a list of lists that determine the range for each variable
    (eg. [[0,4], [0,5], [1,2]] would correspond to 0 <= a <= 4, 0 <= b <= 5, and 1 <= c <= 2 for a + b + c = target).
    target: the value to be added to
    (eg. a target of 15 would correspond to a + b + c = 15).
'''

number_of_solutions = 0
def Combinations(range_list, target, cur = 0, iter_list = []):
    if iter_list == []:
        iter_list = [0] * len(range_list)
    if cur == len(range_list) - 1:
        for iter_list[cur] in range(range_list[cur][0], range_list[cur][1] + 1):
            if sum(iter_list) == target:
                print(iter_list)
                global number_of_solutions
                number_of_solutions += 1
    else:
        for iter_list[cur] in range(range_list[cur][0], range_list[cur][1] + 1):
            Combinations(range_list = range_list, target = target, cur = cur + 1, iter_list = iter_list)

def Solutions(range_list, target):
    Combinations(range_list, target)
    global number_of_solutions
    print(number_of_solutions)
    number_of_solutions = 0

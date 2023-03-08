#!/usr/bin/python3
""" Maria and Ben are playing a game  """


def numbers(n):
    """ Determines the integers between 1 and n  """
    nos = []
    chosen = [True] * (n + 1)
    for integer in range(2, n + 1):
        if (chosen[integer]):
            nos.append(integer)
            for i in range(integer, n + 1, integer):
                chosen[i] = False
    return nos


def isWinner(x, nums):
    """ Who Won??  """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        nos = numbers(nums[i])
        if len(nos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None

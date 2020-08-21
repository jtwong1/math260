"""
some code snippets for HW 1.
copy these into your own code files,
(or ignore them, as long as you still
follow the problem requirements.

Less structure will be provided in future assignments;
I've included it here to be clear about
what you are expected to submit.
"""


# For Exercise 1
def build_player_data():
    """ Creates name/player num/batting averages lists
        for an example team.
    """
    names = ["Gunther O'Brian",
             'Workman Gloom',
             'Esme Ramsey',
             'Cornelius Games',
             'Kline Greenlemon',
             'Hotbox Sato',
             'Famous Owens',
             'Jenkins Good']
    nums = [77, 31, 37, 6, 14, 53, 7, 64]
    avgs = [0.40666, 0.118451, 0.400093, 0.335117,
            0.425694, 0.353378, 0.179842, 0.246856]

    return names, nums, avgs


def print_avg():
    """ prints batting averages for the example team """
    ...


# For P1
def prob_list(n, p):
    """ (write a comment) """
    ...
    # return list of probs. [q0,... qn]


def prob(n, p):
    a = 1  # (rename if preferred)
    b = 1
    for k in range(n):
        c = ...
        ...
    # do not use a list of values here;
    # only the variables given

    return c  # return only qn


if __name__ == "__main__":
    ...
    # figure out n such that qn <= 0.5
    # ... display the result ...


# For P2
def rps():
    """ plays games of rock-paper scissors,
        then summarizes the results.
    """
    # do stuff to initialize
    ...

    while ...:
        # play a round of RPS
        ...
        # ask the player to continue

    # summarize the results
    ...


def cpu_move(moves):
    """ returns the move taken by the computer,
    given a list of previous moves.
    """
    # Note that you can modify this to take in
    # two lists (of player/cpu moves) instead.
    move = 0
    return move

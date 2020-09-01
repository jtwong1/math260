"""
Example solution code for HW 1: rps()

Note that there are alternate ways to write much of the
code in the homework problems - I've supplied one in the
solutions, but don't take this to mean it's the *only way*.
"""
import random


def rps():
    """ plays games of rock-paper scissors,
        then summarizes the results.
    """
    active = 'y'
    moves = []
    shapes = ['rock', 'paper', 'scissors']
    k = 0
    win = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
    while active == 'y':

        p = ''
        while p not in ['0', '1', '2']:
            p = input('Enter move (0=rock, 1=paper, 2=scissors): ')

        c = cpu_move(moves)
        p = int(p)
        moves.append((p, c))
        k += 1

        print(f"{shapes[p]} vs. {shapes[c]}", end="")
        if win[p][c] == 1:
            print("... You win!")
        elif win[p][c] == -1:
            print("... You lose!")
        else:
            print("... tied!")

        active = ''
        while active not in ['y', 'n']:
            active = input("Play again (y/n)? ")

    summary(moves, win)


def summary(moves, win):
    """ Summarize the result of the game,
        given the move list and win table
    """
    shapes = ['rock ', 'paper', 'sciss']  # for display
    n = len(moves)
    print("you \t \t cpu \t outcome")
    score = 0
    losses = 0
    for k in range(n):
        p, c = moves[k]
        w = win[p][c]
        if w == 1:
            out = '+'
            score += 1
        elif w == 0:
            out = '-'
        else:
            out = 'x'
            losses += 1
        print(f"{shapes[p]} \t {shapes[c]} \t {out}")

    print(f"Player wins: {score}/{n}, pct = {100*score/n:.1f}%")
    print(f"cpu wins: {losses}/{n}, pct = {100*losses/n:.1f}%")


def cpu_move(moves):
    """ returns the move taken by the computer,
    given a list of previous moves.
    """

    # (this method wasn't thoroughly tested, just an example...)
    # with no prior info, or 10% of the time,
    # pick a random move
    move = 0
    if len(moves) < 2 or random.randint(0, 10) == 0:
        move = random.randint(0, 2)
    else:
        # otherwise, pick the move that beats the prev.
        # player move or prev. prev. player move,
        # chosen at random.
        prev = moves[-1][0]  # prev player move
        pprev = moves[-2][0]  # prev prev player move

        if random.randint(0, 1) == 1:
            move = (prev + 1) % 3
        else:
            move = (pprev + 1) % 3

    return move

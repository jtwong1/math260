"""
Example solution code for HW 1: Exercise plus prob question

Note that there are alternate ways to write much of the
code in the homework problems - I've supplied one in the
solutions, but don't take this to mean it's the *only way*.
"""


# ------ Exercise 1 ------
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
    names, nums, avgs = build_player_data()
    print("name \t # \t avg")
    for k in range(len(names)):
        print(f"{names[k]} \t {nums[k]:d} \t {avgs[k]:.3f}")

    print("\nVersion 2 (with space adjustments): \n")
    maxlen = max([len(n) for n in names]) + 4
    for k in range(len(names)):
        spaces = " "*(maxlen - len(names[k]))
        print("{}{} {:d} \t {:.3f}".format(
              names[k], spaces, nums[k], avgs[k]))


# ------ Problem 1 ------
def prob_list(n, p):
    """ Computes the probability q_n for P1.
        Returns: a list of [q0, q1, ..., qn]
    """
    q = [0]*(n+1)
    q[0] = 1
    q[1] = 1

    for k in range(2, n+1):
        q[k] = (1-p)*q[k-1] + p*(1-p)*q[k-2]

    return q


def prob(n, p):
    """ Variant of prob_list, without computing the list """
    a = 1
    b = 1

    for k in range(1, n):
        c = (1-p)*a + p*(1-p)*b
        b = a
        a = c

    return c


def prob_search(p, thresh):
    """ Alternate solution: search for k such that q_k <= thresh directly.
        Same as prob, but stops when q_k is below thresh.
    """
    a = 1
    b = 1
    c = 1

    k = 1
    kmax = 100000  # max. k to stop infinite loops
    while k < kmax and c > thresh:
        c = (1-p)*a + p*(1-p)*b
        b = a
        a = c
        k += 1

    return c, k


if __name__ == "__main__":
    thresh = 0.5  # look for q_n <= thresh
    a = (4/52)*(3/51)
    n = 100000
    qlist = prob_list(n, a)
    k = 0  # crude search [better ways possible!]
    while qlist[k] > thresh:
        k += 1
    print(f"\n V1: q[k] <= 0.5 first when k={k}")

    # Alternate way: check as it computes (the efficient way)
    c, k = prob_search(a, thresh)
    print(f"\n V2: q[k] <= 0.5 first when k={k}")

# a few examples of try/except from class

def ex1():
    done = False
    while not done:
        try:
            x = input('enter an integer: ')
            y = int(x)
            done = True
        except ValueError:
            print('invalid! Try again.')
        except KeyboardInterrupt:
            print('Try again!!!!')
    return y


def search(arr, x):
    """ binary search for x in sorted array arr """

    ind = 0
    if x < arr[0] or x > arr[-1]:
        raise ValueError("x is not in the array range!")

    # ind = arr[len(arr)] # create an index error
    # implementation here
    ...
    return ind


def attempt():
    """ Example to show how try/except/finally blocks work """
    arr = [1, 2, 3, 4, 5]
    x = 7
    try:
        ind = search(arr, x)
    except Exception:
        print(" 'Exception' catches every error...")
        # Catching the base exception intercepts any
        # error - unlikely to be what you want!
    except IndexError:
        print(" 'IndexError' Shouldn't happen!")
        # this error isn't raised by search;
        # leave it out [so it doesn't catch typos]
    except ValueError:
        ...
        print(" 'ValueError' x was the wrong size!")
        # ... do something to recover
    finally:
        print(" 'finally' An error occurred!")

    return ind

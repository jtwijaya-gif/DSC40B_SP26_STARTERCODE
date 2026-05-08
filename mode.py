def mode(numbers):
    """
    Efficiently finds the mode of a list of numbers.
    """

    counts = {}

    best = None
    best_count = 0

    for x in numbers:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

        if counts[x] > best_count:
            best = x
            best_count = counts[x]

    return best
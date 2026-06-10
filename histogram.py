def histogram(points, bins):
    """Efficiently computes a histogram.

    Assumes that both `points` and `bins` are sorted in ascending order to
    avoid looping through all bins for each point.

    """
    n = len(points)
    result = []
    i = 0

    for start, end in bins:
        count = 0

        while i < n and points[i] < end:
            count += 1
            i += 1

        width = end - start
        density = count / (n * width)
        result.append(density)

    return result
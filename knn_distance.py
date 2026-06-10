import random


def partition(arr, start, stop, pivot_ix):
    pivot = arr[pivot_ix]

    arr[pivot_ix], arr[stop - 1] = arr[stop - 1], arr[pivot_ix]

    middle = start

    for i in range(start, stop - 1):
        if arr[i][0] < pivot[0]:
            arr[i], arr[middle] = arr[middle], arr[i]
            middle += 1

    arr[middle], arr[stop - 1] = arr[stop - 1], arr[middle]

    return middle


def quickselect(arr, k, start, stop):
    pivot_ix = random.randrange(start, stop)

    pivot_ix = partition(arr, start, stop, pivot_ix)

    if pivot_ix == k:
        return arr[pivot_ix]

    elif pivot_ix < k:
        return quickselect(arr, k, pivot_ix + 1, stop)

    else:
        return quickselect(arr, k, start, pivot_ix)


def knn_distance(arr, q, k):
    """Compute the kth nearest point and the distance to it."""
    
    distances = []

    for x in arr:
        distance = abs(x - q)
        distances.append((distance, x))

    return quickselect(distances, k - 1, 0, len(distances))
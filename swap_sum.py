def swap_sum(A, B):
    """Swaps two elements in two sorted arrays to obtain a target sum 
    difference of 10.

    Assumes that both arrays are sorted in ascending order and only 
    contain integers.

    """
    sum_A = sum(A)
    sum_B = sum(B)

    target = (10 + sum_A - sum_B) / 2

    i = 0
    j = 0

    while i < len(A) and j < len(B):
        diff = A[i] - B[j]

        if diff == target:
            return (i, j)

        elif diff < target:
            i += 1

        else:
            j += 1

    return None
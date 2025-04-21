from counting_sort import counting_sort


def radix_sort(A):
    u = 1 + max(x for x in A)
    n = len(A)                                  # number for dividing -> A[i] // n // n ...
    c = 1 + (u.bit_length() // n.bit_length())  # how many digits in (), e.g: (i, j, k) <- c = 3

    class Obj:                                  # save the attributes
        pass

    D = [Obj() for a in A]                      # turn A[int] 2 D[Obj()]

    for i in range(n):
        D[i].digit = []     # e.g: c = 5, A[i] = 3 -> digit = (3, 0, 0)
        D[i].item = A[i]
        high = A[i]         # use for dividing each time

        for j in range(c):
            high, low = divmod(high, n)         # divide and mod combining function
            D[i].digit.append(low)              # save the mod number, from the least to the most

    for i in range(c):                          # i -> each place, e.g: (i, j, k) -> least significant 2 most
        for j in range(n):                      # each item
            D[j].key = D[j].digit[i]            # this D[].key will save for function: c_s(D, 'key') below
        counting_sort(D, key=lambda x: x.key)   # key means the position would like to compare
    # least significant to most significant, so index started from 0, the least.

    for i in range(n):
        A[i] = D[i].item

    return A


ans = radix_sort([329, 457, 657, 839, 436, 720, 355])
print(ans)

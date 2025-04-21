def counting_sort(A, key=lambda x: x):
    u = 1 + max([key(x) for x in A])    # key() is a lambda function has declared at line 1

    D = [[] for i in range(u)]      # the worst situation is all items save in the same D[key(x)]

    for x in A:
        D[key(x)].append(x)
#    return D                        # [[0], [], [2], [], [4], [], [6], [], [8]]
# D[i], D[k], D[j]

    i = 0
    for chain in D:
        for x in chain:
            A[i] = x
            i += 1
    return A                        # [0, 2, 4, 6, 8]


counting_sort([2, 6, 8, 4, 0])


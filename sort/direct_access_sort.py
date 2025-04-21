def direct_access_sort(A):
    u = 1 + max([x for x in A])       # actually x in fount is x.key
    D = [None] * u
    for x in A:
        D[x] = x                    # D[x.key] = x

#    return D                        # [None, 1, 2, None, 4, 5, 6]
    i = 0
    for key in range(u):
        if D[key] is not None:
            A[i] = D[key]
            i += 1
    return A                        # [1, 2, 4, 5, 6]


ans = direct_access_sort([2, 5, 6, 4, 1])
print(ans)

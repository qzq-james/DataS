# merge sort

def merge_sort(A, a=0, b=None):
    if b is None:  b = len(A)
    if 1 < b - a:   # push b-a = len(A) -> b-a = half of len(A) until 1, while recurve can reach every node
        c = (a + b + 1) // 2    # math: using c to push a and b to upper
        merge_sort(A, a, c)     # quite complicate, only remember when it comes to 1 (not<) b - a,
        merge_sort(A, c, b)     # then go to this line, every step will be recorded for next a, b
        L, R = A[a:c], A[c:b]   # then using the last a, b, c
        merge(L, R, A, len(L), len(R), a, b)
    return A
# when everytime reach the second merge_sort, c, b -> a, b, then cal c and go to the first merge_sort again


# called two-finger algorithm: using L, R to compare and cover the item of A's
def merge(L, R, A, i, j, a, b):
    if a < b:
        if (j == 0) or (i > 0 and L[i - 1] > R[j - 1]):     # j == 0 means only L[i] elements are redundant
            A[b - 1] = L[i - 1]     # -> the condition i > 0 no need to reach the equal 0 situation
            i -= 1
        else:
            A[b - 1] = R[j - 1]
            j -= 1
        merge(L, R, A, i, j, a, b - 1)


ans = merge_sort([7, 1, 4, 3, 5, 8, 9, 0])
print(ans)

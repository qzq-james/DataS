# selection sort

def selection_sort(A, i=None):
    if i is None:   i = len(A) - 1  # only declara once at the beginning
    if i > 0:
        j = find_max(A, i)          # always the biggest
        A[i], A[j] = A[j], A[i]     # exchange
        selection_sort(A, i-1)      # recursive
    return A                        # everything has done


# using recursive to replace (if condition plus loop), and it is better
def find_max(A, i):
    if i > 0:
        j = find_max(A, i-1)    # first go to only i = 0, and start to go back, i = 1, i = 2 until the boundary i = i
        if A[i] < A[j]:         # each time compare the previous(j) and now(i)
            return j            # if condition is yes, return j;
    return i                    # no, return i


# total
ans = selection_sort([8, 5, 4, 3, 9])
print(ans)

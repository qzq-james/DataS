# insertion sort

def insertion_sort(A, i=None):
    if i is None: i = len(A) - 1
    if i > 0:
        sort(A, i)
        insertion_sort(A, i - 1)
    return A


def sort(A, i):
    if i > 0:
        for j in range(1, i):                   # everytime from front until the boundary
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]     # if previous bigger than current(j), exchange


ans = insertion_sort([2, 0, 1, 3, 9])
print(ans)

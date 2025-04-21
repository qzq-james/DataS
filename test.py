def counting_sort(arr, key=lambda x: x):
    if not arr:
        return []

    # Get the maximum key value
    max_key = max(key(x) for x in arr)

    # Initialize count array
    count = [0] * (max_key + 1)

    # Count occurrences of each key
    for item in arr:
        count[key(item)] += 1

    # Compute cumulative counts
    for i in range(1, max_key + 1):
        count[i] += count[i - 1]

    # Build the output array
    output = [None] * len(arr)
    for item in reversed(arr):
        output[count[key(item)] - 1] = item
        count[key(item)] -= 1

    return output


def radix_sort(A):
    if not A:
        return []

    u = 1 + max(x for x in A)
    n = len(A)
    c = 1 + (u.bit_length() // n.bit_length())

    class Obj:
        pass

    D = [Obj() for _ in A]

    for i in range(n):
        D[i].digit = []
        D[i].item = A[i]
        high = A[i]
        for _ in range(c):
            high, low = divmod(high, n)
            D[i].digit.append(low)

    for i in range(c):
        for j in range(n):
            D[j].key = D[j].digit[i]
        D = counting_sort(D, key=lambda x: x.key)

    for i in range(n):
        A[i] = D[i].item

    return A


# Test the function
arr = [32, 3, 44, 42, 22]
sorted_arr = radix_sort(arr.copy())
print(f"Original array: {arr}")
print(f"Sorted array: {sorted_arr}")
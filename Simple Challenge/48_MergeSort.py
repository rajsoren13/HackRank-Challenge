def mergeProcedure(arr, i, mid, j):
    # number of elements in left subarray: indices i..mid
    n1 = mid - i + 1
    # number of elements in right subarray: indices mid+1..j
    n2 = j - mid

    # build temporary left and right subarrays by copying from arr
    leftSubarray = [0] * n1
    rightSubarray = [0] * n2

    for m in range(n1):
        leftSubarray[m] = arr[i + m]      # arr[i], arr[i+1], ..., arr[mid]

    for m in range(n2):
        rightSubarray[m] = arr[mid + 1 + m]  # arr[mid+1], ..., arr[j]

    # merge leftSubarray and rightSubarray back into arr[i..j]
    x = 0   # pointer into leftSubarray
    y = 0   # pointer into rightSubarray
    k = i   # pointer into arr — where we write the next merged element

    while x < n1 and y < n2:
        if leftSubarray[x] <= rightSubarray[y]:
            arr[k] = leftSubarray[x]
            x += 1
        else:
            arr[k] = rightSubarray[y]
            y += 1
        k += 1

    # copy any leftover elements from leftSubarray
    while x < n1:
        arr[k] = leftSubarray[x]
        x += 1
        k += 1

    # copy any leftover elements from rightSubarray
    while y < n2:
        arr[k] = rightSubarray[y]
        y += 1
        k += 1


def mergeSort(arr, i, j):
    if i >= j:          # base case: 0 or 1 elements — nothing to sort
        return arr
    else:
        mid = i + (j - i) // 2
        mergeSort(arr, i, mid)
        mergeSort(arr, mid + 1, j)
        mergeProcedure(arr, i, mid, j)
    return arr


# ---- Example run ----
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    mergeSort(data, 0, len(data) - 1)
    print("Sorted array:", data)
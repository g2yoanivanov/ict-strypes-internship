def merge(arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid

    left = [0] * n1
    right = [0] * n2

    for i in range(n1):
        left[i] = arr[start + i]

    for j in range(n2):
        right[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = start

    while i < n1 and j < n2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, start, end):
    if start < end:
        mid = start + (end - start) // 2

        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr_m = [12, 62, 23, 77, 1, 6, 10]
    arr_b = [11, 5, 29, 30, 2, 12, 7]

    merge_sort(arr_m, 0, len(arr_m) - 1)
    for x in arr_m:
        print(x, end=' ')

    print('\n')

    bubble_sort(arr_b)
    for x in arr_b:
        print(x, end=' ')
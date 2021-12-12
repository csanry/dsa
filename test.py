def selection_sort(array, size):

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # change > to < to sort in descending order
            # selects the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
                # once the min value is found, swap with min_idx
        array[step], array[min_idx] = array[min_idx], array[step]


arr = [4, 2, 1, 3, 6, 8, 5, 7]

selection_sort(arr, len(arr))

print(arr)
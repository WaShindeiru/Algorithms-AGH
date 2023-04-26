def SelectionSort(data):
    for i in range(len(data)):

        min_idx = i

        for x in range(i+1, len(data), 1):
            if data[min_idx] > data[x]:
                min_idx = x

        data[i], data[min_idx] = data[min_idx], data[i]

    return data
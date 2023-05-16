def InsertionSort(tab):

    array = tab[:]
    size = len(array)

    for i in range(1, size):

        key = array[i]
        j = i-1

        while j>=0 and array[j] > key:
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1

    return array

def main():
    array_to_sort = [2345, 456,1567, 12345,4567,1234,3456,2345]
    print(InsertionSort(array_to_sort))
    print(array_to_sort)

if __name__ == "__main__":
    main()
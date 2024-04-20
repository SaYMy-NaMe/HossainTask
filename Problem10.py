def sort(array, size):
    # performing bubble sort here
    for i in range(size-1):
        for j in range(i+1, size):
            if array[i] > array[j]:
                # swapping two number without declaring third variable
                array[j] = array[j] + array[i]
                array[i] = array[j] - array[i]
                array[j] = array[j] - array[i]


def main():
    array = [10, 22, -5, 117, 0]
    size = len(array)
    sort(array, size)
    for i in range(size):
        print(array[i], end=" ")


if __name__ == "__main__":
    main()

mean = 0


def take_input(array, n):
    for i in range(n):
        element = int(input())
        array.append(element)


def calc_std_deviation(array, n):
    global mean
    deviation = 0
    for element in array:
        deviation += (element - mean) ** 2
    deviation = deviation / n
    std_deviation = deviation ** 0.5
    return std_deviation


def calc_mean(array, n):
    global mean
    summ = 0
    for element in array:
        summ += element
    mean = summ / n


def main():
    array = []
    n = int(input())
    take_input(array, n)
    calc_mean(array, n)
    std_deviation = calc_std_deviation(array, n)
    print("{:.2f}".format(std_deviation))  # Print standard deviation up to 2 decimal places


if __name__ == "__main__":
    main()

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generate_prime(number):
    primes = []
    for i in range(1, number):
        flag = is_prime(i)
        if flag:
            primes.append(i)
    print("Prime less than ", number, ":", end=" ")

    # Prime Printing according to the Document
    for i in range(0, len(primes) - 1):
        print(primes[i], end=",")
    print(primes[len(primes) - 1])


def main():
    number = int(input())
    generate_prime(number)


if __name__ == "__main__":
    main()

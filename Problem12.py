def is_prime(number):
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_prime(number):
    primes = []
    for i in range(1, number):
        flag = is_prime(i)
        if flag:
            primes.append(i)
    print(primes)


def main():
    number = int(input())
    generate_prime(number)


if __name__ == "__main__":
    main()

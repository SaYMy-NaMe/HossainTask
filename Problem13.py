def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def gen_nth_prime(nth_digit):
    no_primes = 0
    i = 1
    while True:
        flag = is_prime(i)
        if flag:
            no_primes += 1
            if no_primes == nth_digit:
                print(i)
                break
        i += 1


def main():
    nth_digit = int(input())
    gen_nth_prime(nth_digit)


if __name__ == "__main__":
    main()

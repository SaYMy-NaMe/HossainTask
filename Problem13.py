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
            if nth_digit % 100 // 10 == 1:
                print(nth_digit, "th Prime:", i)
            else:
                if nth_digit % 10 == 1:
                    print(nth_digit, "st Prime:", i)
                elif nth_digit % 10 == 2:
                    print(nth_digit, "nd Prime:", i)
                elif nth_digit % 10 == 3:
                    print(nth_digit, "rd Prime:", i)
                else:
                    print(nth_digit, "th Prime:", i)
            break
        i += 1


def main():
    nth_digit = int(input())
    gen_nth_prime(nth_digit)


if __name__ == "__main__":
    main()

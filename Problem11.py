def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def main():
    number = int(input())
    flag = is_prime(number)
    if flag:
        print(number, "is Prime")
    else:
        print(number, "is not Prime")


if __name__ == "__main__":
    main()

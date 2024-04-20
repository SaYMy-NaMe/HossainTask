def find_substr(a, b):
    if b in a:
        return 1
    else:
        return -1


def main():
    a = input()
    b = input()
    flag = find_substr(a, b)
    print(flag)


if __name__ == "__main__":
    main()

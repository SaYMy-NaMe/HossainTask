def find_substr(maxi, minn):
    if minn in maxi:
        return 1
    else:
        return -1


def main():
    a = input()
    b = input()
    if len(b) < len(a):
        flag = find_substr(a, b)
    else:
        flag = find_substr(b, a)
    print(flag)


if __name__ == "__main__":
    main()

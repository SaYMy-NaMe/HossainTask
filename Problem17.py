def GCD(a, b):
    while True:
        rem = a % b
        if rem == 0:
            return b
        a = b
        b = rem


def LCM(a, b, gcd):
    lcm = (a * b) // gcd
    return lcm


def main():
    while True:
        a = int(input())
        b = int(input())
        gcd = GCD(a, b)
        lcm = LCM(a, b, gcd)
        print("GCD: ", gcd)
        print("LCM: ", lcm)


if __name__ == "__main__":
    main()

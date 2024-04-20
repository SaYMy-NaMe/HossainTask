converted_list = []


def show_converted_number():
    converted = "";
    for x in converted_list:
        if x == 10:
            converted += "A"
        elif x == 11:
            converted += "B"
        elif x == 12:
            converted += "C"
        elif x == 13:
            converted += "D"
        elif x == 14:
            converted += "E"
        elif x == 15:
            converted += "F"
        else:
            converted += str(x);
    print(converted[::-1])


def convert_number(n, b):
    while n != 0:
        converted_list.append(n % b)
        n //= b
    show_converted_number()


def get_number_and_base():
    n = int(input())
    b = int(input())
    if 2 <= b <= 16:
        convert_number(n, b)
    else:
        print("Base not within proper range!")


def main():
    get_number_and_base()


if __name__ == "__main__":
    main()

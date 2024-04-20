matrix = []
m = 3
n = 5


def input_matrix():
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input())
            row.append(element)
        matrix.append(row)


def show_matrix():
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


def scalar_multiply(scalar):
    for i in range(m):
        for j in range(n):
            matrix[i][j] = matrix[i][j] * scalar


def main():
    input_matrix()
    print("Original: ")
    show_matrix()
    scalar = int(input())
    scalar_multiply(scalar)
    print("Multiplied by ", scalar, ": ")
    show_matrix()


if __name__ == "__main__":
    main()

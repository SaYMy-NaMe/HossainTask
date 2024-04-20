matrix = []


def input_matrix(m, n):
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input())
            row.append(element)
        matrix.append(row)


def show_matrix(m, n):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


def scalar_multiply(scalar, m, n):
    for i in range(m):
        for j in range(n):
            matrix[i][j] = matrix[i][j] * scalar


def main():
    m = int(input())
    n = int(input())
    input_matrix(m, n)
    print("Original: ")
    show_matrix(m, n)
    scalar = int(input())
    scalar_multiply(scalar, m, n)
    print("Multiplied by ", scalar, ": ")
    show_matrix(m, n)


if __name__ == "__main__":
    main()

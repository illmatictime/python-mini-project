def setZero(aList):
    for x in range(len(aList)):
        aList[x] = 0


def inputArray(alpha):
    print("Enter 20 integers:")
    for x in range(20):
        alpha[x] = int(input())


def doubleArray(alpha, beta):
    for x in range(len(alpha)):
        beta[x] = 2 * alpha[x]


def copyGamma(gamma, inStock):
    # inStock[0] = gamma.copy()
    for x in range(len(gamma)):
        inStock[0][x] = gamma[x]
    for row in range(1, 10):
        for column in range(len(gamma)):
            inStock[row][column] = 3 * inStock[row - 1][column]


def copyAlphaBeta(alpha, beta, inStock):
    for row in range(5):
        for column in range(4):
            inStock[row][column] = alpha[(row * 4) + column]
    for row in range(5, 10):
        for column in range(4):
            inStock[row][column] = beta[((row * 4) + column) - 20]


def printArray(aList):
    for x in range(len(aList)):
        print(aList[x], end="\t")
    # print("\n\n")
    # print(*aList, sep='\t')


def setInStock(aList, delta):
    print("Enter 10 integers:")
    for row in range(len(aList)):
        aList[row][0] = int(input())
    for row in range(len(aList)):
        for column in range(1, len(aList[0])):
            aList[row][column] = (2 * aList[row][column - 1]) - delta[row]


def main():
    inStock = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
               [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
               [0, 0, 0, 0], [0, 0, 0, 0]]
    alpha = list(range(1, 21))
    print("Alpha after initialization:")
    printArray(alpha)
    print("\n\n")

    beta = list(range(1, 21))
    gamma = [11, 13, 15, 17]
    delta = [3, 5, 2, 6, 10, 9, 7, 11, 1, 8]
    setZero(alpha)
    setZero(beta)

    inputArray(alpha)
    print("Alpha after reading 20 numbers:")
    printArray(alpha)
    print("\n\n")

    doubleArray(alpha, beta)
    print("Beta after a call to doubleArray:")
    printArray(beta)
    print("\n\n")

    copyGamma(gamma, inStock)
    print("inStock after a call to copyGamma:")
    for x in range(len(inStock)):
        printArray(inStock[x])
        print()
    print("\n\n")

    copyAlphaBeta(alpha, beta, inStock)
    print("inStock after a call to copyAlphaBeta:")
    for x in range(len(inStock)):
        printArray(inStock[x])
        print()
    print("\n\n")

    setInStock(inStock, delta)
    print("inStock after a call to setInStock:")
    for x in range(len(inStock)):
        printArray(inStock[x])
        print()
    print("\n\n")


main()

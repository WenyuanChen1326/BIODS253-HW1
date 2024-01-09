import numpy as np


def pascal(n: int = 15):
    for i in range(n):
        for j in range(i + 1):
            print(
                np.math.factorial(i) / (np.math.factorial(j) * np.math.factorial(i - j))
            )
        print("  ")


if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    pascal(n)

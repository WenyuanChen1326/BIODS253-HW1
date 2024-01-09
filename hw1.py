import numpy as np
def pascal(n = 10):
    for i in range(n):
        for j in range(i+1):
            print(np.math.factorial(i)/(np.math.factorial(j)*np.math.factorial(i-j)))
        print("  ")
def main():
    # print (pascal())
    pascal()
if __name__ == "__main__":
    main()
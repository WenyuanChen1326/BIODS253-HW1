import sys
import time

import numpy as np
import pandas as pd


def pascal(n: int = 15):
    for i in range(n):
        for j in range(i + 1):
            print(
                np.math.factorial(i) / (np.math.factorial(j) * np.math.factorial(i - j))
            )
        print("  ")


def runtime_analysis(n_repeats: int = 100, n_rows: int = 15):
    timing_metrics = []
    for n in range(n_rows):
        for i in range(n_repeats):
            start = time.time()
            pascal(n)
            end = time.time()
            timing_metrics.append({"Number of rows": n, "Time (s)": end - start})

    return pd.DataFrame(timing_metrics)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Take in n_rows as command line argument with default value of 15
    n_rows = int(sys.argv[1]) if len(sys.argv) > 1 else 15

    # Run pascal's triangle with input n_rows
    pascal(n=n_rows)

    # Do runtime analysis and plot
    timing_results = runtime_analysis()
    sns.lineplot(data=timing_results, x="Number of rows", y="Time (s)")
    plt.show()

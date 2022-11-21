import numpy as np
import time


def main():
    for i in range(1000000):
        d = np.sqrt(np.sqrt(i))


if __name__ == "__main__":
    start = time.perf_counter()
    b = main()
    end = time.perf_counter()
    print(b)
    print(f'Time needed for the summing is: {end-start} seconds')

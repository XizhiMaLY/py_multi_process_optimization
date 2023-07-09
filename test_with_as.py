"""
This module demenstrate a simple way for multiprocessing.
"""
from multiprocessing import Pool
import time
def f(x):
    return x*x

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        lt = pool.map(f, range(10))
        time.sleep(10)
    print(lt)


import time


def calc_time_elapsed(func):
    def wrapper(obj):

        start = time.time()
        func(obj)
        end = time.time()
        return end - start
    return wrapper 
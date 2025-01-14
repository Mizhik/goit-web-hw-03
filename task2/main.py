from multiprocessing import Pool, cpu_count
from time import time

def factorize_sync(*numbers):
    result = []
    for num in numbers:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        result.append(factors)
    return result


def factorize_parallel(*numbers):
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(factorize_sync, numbers)
    return results

if __name__ == "__main__":
    a, b, c, d = factorize_sync(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    start_time = time()
    factorize_sync(128, 255, 99999, 10651060)
    end_time = time()
    print("Час виконання синхронної версії:", end_time - start_time)

    a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    start_time = time()
    factorize_parallel(128, 255, 99999, 10651060)
    end_time = time()
    print("Час виконання паралельної версії:", end_time - start_time)


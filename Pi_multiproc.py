#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import multiprocessing

count_pool = 10
count_points = 10000
def random_points(n):
    count = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x*x + y*y <= 1:
            count = count + 1
    return count

def test_all(pool):
    l = pool.map(random_points, [count_points]*count_pool)
    return l

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    count = sum(test_all(pool))
    print(4 * count/(count_points*count_pool))
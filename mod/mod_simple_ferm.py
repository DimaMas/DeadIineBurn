import math
import random

def is_simple_ferm(a, count):
        for i in range(count):
            rd = random.randint(1, a - 1)
            if (rd ** (a - 1) % a != 1):
                return False
        return True

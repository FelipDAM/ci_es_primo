import math


def es_primo(Num):
    if Num < 2:
        return False
    for n in range(2, math.floor(math.sqrt(Num) + 1)):
        if Num % n == 0:
            return False
    return True
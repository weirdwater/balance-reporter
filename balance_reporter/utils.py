from typing import TypeVar

a = TypeVar('a')

def tail(l: list[a]) -> a:
    if (len(l) == 0):
        raise Exception("Array is empty")
    return l[len(l) - 1]

def head(l: list[a]) -> a:
    if (len(l) == 0):
        raise Exception("Array is empty")
    return l[0]

import os
import psutil

from collections import namedtuple
from collections import defaultdict
from collections import deque


# task with using namedtuple
def operations(arg1: int, arg2: int):
    Operations = namedtuple("Operations", ["sum", "concat", "mul", "div"])
    return Operations(
        arg1 + arg2,
        str(arg1) + str(arg2),
        arg1 * arg2,
        arg1 / arg2,
    )


# task with using defaultdict
s = [["d", 0], ["i", 1], ["c", 2], ["t", 3]]
d = defaultdict(lambda: defaultdict(int))

d[0][1] += 1

print(d)
print(d[4][1])
print(d[0][2])


def append_left_deque():
    numbers = deque(range(1, 10000000))
    numbers.appendleft(0)
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0] / 2.0 ** 30
    print("memory use:", memoryUse)
    return numbers


def append_left_list():
    numbers = list(range(1, 10000000000000))
    numbers.insert(0, 0)
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0] / 2.0 ** 30
    print("memory use:", memoryUse)
    return numbers
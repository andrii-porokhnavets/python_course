import random


def generate_list_of_random(length):
    return [random.randint(0, 1000) for i in range(length)]


def sum_of_list(arr):
    s = 0
    for a in arr:
        s += a

    return s


def average_of_list(arr):
    return sum_of_list(arr) / len(arr)


a = generate_list_of_random(10)
s = sum_of_list(a)
av = average_of_list(a)

print(a, s, av)


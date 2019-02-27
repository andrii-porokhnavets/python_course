import random

x = 10
my_list = [random.randint(0, 1000) for i in range(x)]

sum_of_list = 0
for n in my_list:
    sum_of_list += n

average = sum_of_list / len(my_list)

print(my_list)
print(sum_of_list)
print(average)

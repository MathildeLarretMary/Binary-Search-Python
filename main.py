"""import random

def random_list(min_v, max_v, length) -> list:
    my_list = []
    for i in range(length):
        rand = random.randint(min_v, max_v)
        my_list.append(rand)

    return my_list


lis = random_list(1, 55, 15)
print(lis)
lis.sort()
print(lis)"""

lis = [1, 2, 5, 6, 10, 17, 18, 21, 24, 30, 32, 46, 46, 53, 55]

print(lis)


def binary_search(the_list, v, i_min, i_max):

    # if there is only one element in array
    if i_max-i_min == 0:
        if the_list[i_min] == v:
            return i_min
        return -1

    # if there is only two elements in array
    if i_max-i_min == 1:
        if the_list[i_min] == v:
            return i_min
        elif the_list[i_max] == v:
            return i_max
        else:
            return -1

    # if there is more than two elements in array
    i_center = (i_max + i_min) // 2
    if the_list[i_center] == v:
        return i_center
    elif the_list[i_center] < v:
        return binary_search(the_list, v, i_center+1, i_max)
    else:
        return binary_search(the_list, v, i_min, i_center-1)


# TODO: change only this value to test
search = 32

print(binary_search(lis, search, 0, len(lis) - 1))

# 1

# import random

# def random_list(n, a, b):
#     return [random.randint(a, b) for i in range(n)]
# list1 = random_list(10, 5, 15)
# print(list1)

# 2

# def find_max(lst1):
#     return max(list1)
# list1 = [3, 7, 2, 9, 1, 5]
# print(find_max(list1))


# def find_max(lst1):
#     max_value = 0
#     for num in list1:
#         if num > max_value:
#             max_value = num
#     return max_value

# numbers = [3, 7, 2, 9, 1, 5]
# print(find_max(numbers))

# 3

# def count_dup(lst1):
#     return len(list1) - len(set(list1))
# list1 = [1, 2, 3, 2, 4, 3, 3, 5]
# print(count_dup(numbers))

# 4

# def positive_numbers(numbers):
#     positive_numbers = []
#     for i in numbers:
#         if i > 0:
#             positive_numbers.append(i)
#     return positive_numbers

# list1 = [5, -2, 10, -8, 3, 0, -1, 7]
# result = positive_numbers(list1)
# print(result)


# # 5

# def remove_even_numbers(numbers):
#     odd_numbers = []
#     for i in numbers:
#         if i % 2 != 0:
#             odd_numbers.append(i)
#     return odd_numbers
# list1 = [5, -2, 10, -8, 3, 0, -1, 7]
# result = remove_even_numbers(list1)
# print(result)


# # 6

# def combine_unique(lst1, lst2):

#     return list(set(lst1 + lst2))

# list1 = [5, -2, 10, -8, 3, 0, -1, 7]
# list2 = [1, 2, 3, 2, 4, 3, 3, 5]
# print(combine_unique(list1, list2))
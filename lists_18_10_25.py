list1 = [5, 8, 12, 6, 7]
list2 = [4, 5, 9, 12, 11]

# 1

# for i in list1:
#     flag = False
#     for j in list2:
#         if i == j:
#             flag = True
#     if not flag:
#         print(i)

# 2

# for i in list1:
#     flag = False
#     for j in list2:
#         if i == j:
#             flag = True
#             print(i)


# 3

# for i in range(len(list1)):
#     for j in range(i + 1, len(list1)):
#         if list1[i] == list1[j]:
#             list1[i] = 0
#             list1[j] = 0
# print(list1)

# 4

# summa1 = 0
# for i in list1:
#     summa1 += i
#     average1 = summa1 / len(list1)
#     for j in list2:
#         summa2 = 0
#         summa2 += j
#         average2 = summa2 / len(list2)
# if average1 > average2:
#     print(average1)
# elif average2 > average1:
#     print(average2)
# else:
#     print("The average is equal")

# 5

# list1 = [5, 8, 2, 6, 7]
# list2 = [1, 5, 9, 3, 4]
#
# for i in range(len(list1)):
#     list1[i] , list2[i] = list2[i], list1[i]
#     print(list1[i], list2[i])





# # Online Python compiler (interpreter) to run Python online.
# # Write Python 3 code in this online editor and run it.
#
# list_elements = [1, 2, 6, -9, -8, 3, -7, 0, 0]
#
#
# # Even index → odd number
# # Odd index → even number
#
#
# def arrange_no(list_elements):
#     new_list = [0] * len(list_elements)
#     p1 = 0
#     p2 = 1
#
#     for i, num in enumerate(list_elements):
#
#         if i % 2 == 0:
#             if num % 2 != 0:
#                 new_list[p1] = num
#                 p1 = p1 + 1
#
#             else:
#                 for j in range(p2, len(list_elements )+ 1):
#                     if abs(list_elements[j]) % 2 == 1:
#                         new_list[p1] = list_elements[p2]
#                     else:
#                         p2 = p2 + 1
#
#         else:
#             if num % 2 == 0:
#                 new_list[p1] = num
#                 p1 = p1 + 1
#             else:
#                 for j in range(p2, len(list_elements) + 1):
#                     if abs(list_elements[j]) % 2 == 0:
#                         new_list[p1] = list_elements[p2]
#                     else:
#                         p2 = p2 + 1
#         p2 = p1
#         p2 = p2 + 1
#
#     return new_list
#
#
# res = arrange_no(list_elements)
#
# print(res)


list_elements = [1, 2, 6, -9, -8, 3, -7, 0, 0]

# Even index → odd number
# Odd index → even number

def arrange_no(elements):
    n = len(elements)
    new_list = [0] * n   # pre-allocated list

    odd_ptr = 0
    even_ptr = 0

    # find first odd and even positions
    while odd_ptr < n and elements[odd_ptr] % 2 == 0:
        odd_ptr += 1

    while even_ptr < n and elements[even_ptr] % 2 != 0:
        even_ptr += 1

    for i in range(n):
        if i % 2 == 0:  # even index → need odd number
            while odd_ptr < n and elements[odd_ptr] % 2 == 0:
                odd_ptr += 1
            if odd_ptr < n:
                new_list[i] = elements[odd_ptr]
                odd_ptr += 1
        else:  # odd index → need even number
            while even_ptr < n and elements[even_ptr] % 2 != 0:
                even_ptr += 1
            if even_ptr < n:
                new_list[i] = elements[even_ptr]
                even_ptr += 1

    return new_list


res = arrange_no(list_elements)
print(res)
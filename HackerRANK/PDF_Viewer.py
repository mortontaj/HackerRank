h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = 'zaba'

_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
small_list = []
largest = 0

for i, j in enumerate(_, len(_)-len(_)):
    if j in word:
        small_list.append(i)

for i in small_list:
    if h[i] > largest:
        largest = h[i]

print(largest * len(word))


# for j in range(len(small_set)):
#     for char in h[small_set[j]]:
#         if char > largest:
#             largest = char
# print(largest * len(word))

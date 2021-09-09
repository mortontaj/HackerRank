aarr = [0, 1, 2, 2, 1, 1, 1, 1]
# print(aarr)
# print()
# print(set(aarr))
#
# print(len(set(aarr)))
# print(len(aarr))

numm = []
pairs = 0
for _ in aarr:
    if aarr.count(_) > 1:
        numm.append(_)

for i in set(numm):
    if numm.count(i) % 2 == 0:
        pairs += (numm.count(i) // 2)
    else:
        pairs += ((numm.count(i) - 1) // 2)

print(pairs)
# print(len(numm))
# print((len(set(numm))))
# print(len(numm) // len(set(numm)))

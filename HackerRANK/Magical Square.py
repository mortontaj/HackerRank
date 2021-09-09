s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

print(sum(s[0]), sum(s[1]), sum(s[2]),)

t = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(s)):
    # iterate through columns
    for j in range(len(s[0])):
        t[j][i] = s[i][j]

for r in t:
    print(r)

print('________')

print(sum(s[0]), sum(s[1]), sum(s[2]),)
print(sum(t[0]), sum(t[1]), sum(t[2]),)
print('________')

ns = ''
addedUp = 0
square = -45
counter = 0
simp = ''

if s[1][1] >= 5:
    addedUp = s[1][1] - 5
    s[1][1] = 5
else:
    addedUp = 5 - s[1][1]
    s[1][1] = 5

for _ in s[0]:
    ns += str(_)
for _ in s[1]:
    ns += str(_)
for _ in s[2]:
    ns += str(_)
ns = ''.join(ns)
print(ns)
print(list(ns))

for i in ns:
    square += int(i)

# if square > 0:
#     addedUp += square
# else:
#     addedUp -= square

for i in range(0, 9):
    if ns.count(ns[i]) > 1:
        addedUp += int(ns[i]) * (ns.count(ns[i]) - 1)
        counter += 1
        if str(ns[i]) not in simp:
            simp += str(ns[i])
    if ns.count(str(i + 1)) == 0:
        addedUp -= i
        counter += 1
        if str(i + 1) not in simp:
            simp += str(i + 1)

# for i in range(0, 9):
    if ns.count(ns[i]) == 1 and not (int(ns[i]) == 5 and i == 4):
        if int(ns[i]) % 2 != int(i) % 2:
            addedUp += i
            if str(ns[i]) not in simp:
                simp += str(ns[i])

print(ns.count(ns[5]), ' count of the number ', ns[5])
print(ns[5], ' number in position of ', 5)
print(simp)

if len(simp) == counter:
    print(abs(square), 'only twooo!')

# else:
print(abs((addedUp - square) - (addedUp + square)))
print(square, ' is square')
print(addedUp, ' is addedUp')
#

#
# for i in range(0,3):
#     for j in range(0,3):
#         if (i + j) % 2 == s[i][j] % 2:
#             s[i][j] =

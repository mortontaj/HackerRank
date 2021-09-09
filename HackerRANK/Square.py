s = [[4, 9, 2],
     [3, 5, 7],
     [8, 1, 5]]

print(sum(s[0]), sum(s[1]), sum(s[2]),)
t = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(len(s)):  # iterate through rows
    for j in range(len(s[0])):  # iterate through columns
        t[j][i] = s[i][j]
for r in t:
    print(r)

x = 0
y = 0
for i in range(0, 3):
    x += (s[i][2 - i])
    y += (s[2 - i][i])
print(t)



# print('________')
# print(sum(s[0]), sum(s[1]), sum(s[2]), " row sums")
# print('________')
# print(sum(t[0]), sum(t[1]), sum(t[2]), " column sums )
# print('________')
# print(y, x " is main and other diagonal. ")


# s[0][2] + s[1][1] + s[2][0]

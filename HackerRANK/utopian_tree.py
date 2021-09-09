period = int(input('What is the period? '))

height = 1
for i in range(1, period+1):
    if i % 2 == 1:
        height *= 2
    if i % 2 == 0:
        height += 1

print(height)
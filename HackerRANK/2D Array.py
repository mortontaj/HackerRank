arr = [[-9, -9, -9, 1, 1, 1],
       [0, -9, 0, 4, 3, 2],
       [-9, -9, -9, 1, 2, 3],
       [0, 0, 8, 6, 6, 0],
       [0, 0, 0, -2, 0, 0],
       [0, 0, 1, 2, 4, 0], ]

counter = 0
for i in range(6):
   for j in range(6):
      if j <= 3 and i <= 3:
         hourglass = (int(arr[i][j]) + int(arr[i][j + 1]) + int(arr[i][j + 2]) +
                    (int(arr[i+1][j + 1])) +
                   int(arr[i+2][j]) + int(arr[i+2][j + 1]) + int(arr[i+2][j + 2]))
      if hourglass > counter:
         counter = hourglass

print(counter)

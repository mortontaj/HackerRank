ar = [1, 1, 2, 2, 3]


def migratoryBirds(arr):
    counter = 0

    for i in sorted(set(arr)):
        bird_type = arr.count(i)
        if bird_type > counter:
            counter = bird_type
            num = i

    return num


zz = migratoryBirds(ar)

print(zz)

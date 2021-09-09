nn, kk = 6, 3
arar = [1, 3, 2, 6, 1, 2]

def divisibleSumPairs(n, k, ar):
    counter = 0
    for i, num in enumerate(ar, len(ar)):
        for j, okk in enumerate(ar, len(ar)):
            if i != j and (okk + num) % k == 0:
                counter += 1

    return counter // 2


jj = divisibleSumPairs(nn, kk, arar)
print(jj)

nn, kk = 4, 1       #     length of bill (i.e len(bill))
#                   #     index (i.e bill[i]

kk = 1              # give but convert to index (i.e bill[i]
billl = [3, 10, 2, 9]   # given
bb = 7  # given


def bonAppetit(bill, k, b):

    tot = 0
    for i in bill:
        tot += i

    if (tot - bill[k]) // 2 == b:
        print('Bon Appetit')

    else:
        print(b - ((tot - bill[k]) // 2))


bonAppetit(billl, kk, bb)

from collections import Counter


def shoe_shop_earnings():
    X = int(input())

    shoe_sizes = list(map(int, input().split()))

    stock = Counter(shoe_sizes)

    N = int(input())
    earnings = 0
    for _ in range(N):
        size, price = map(int, input().split())
        if stock[size] > 0:
            earnings += price
            stock[size] -= 1
    print(earnings)


shoe_shop_earnings()
from collections import Counter

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

OFFERS = {
    'A': [(3, 130)],
    'B': [(2, 45)]
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_counter = Counter(skus)
    print(sku_counter)


if __name__ == '__main__':
    order1 = 'ABC'
    assert checkout(order1) == 100


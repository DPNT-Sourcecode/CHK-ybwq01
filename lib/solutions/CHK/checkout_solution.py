from collections import Counter

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

OFFERS = {
    'A': {3: 130},
    'B': {2: 45}
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    sku_counter = Counter(skus)
    for sku in sku_counter:
        count_sku = sku_counter[sku]
        if sku in OFFERS:
            offers = sorted(OFFERS[sku].keys(), reverse=True)
            for offer in offers:
                while offer >= count_sku:
                    total += OFFERS[sku][offer]
                    count_sku -= offer

    return total

if __name__ == '__main__':
    order1 = 'ABC'
    assert checkout(order1) == 100



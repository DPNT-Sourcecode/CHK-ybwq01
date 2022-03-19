from collections import Counter

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}

OFFERS = {
    'A': {3: 130, 5: 200},
    'B': {2: 45}
}

CROSS_OFFERS = {
    'E': {2: {'B': 1}}
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    sku_counter = Counter(skus)
    for sku in sku_counter.keys():
        if sku not in PRICES:
            return -1
        count_sku = sku_counter[sku]
        if sku in OFFERS:
            offers = sorted(OFFERS[sku].keys(), reverse=True)
            for offer in offers:
                while count_sku >= offer:
                    total += OFFERS[sku][offer]
                    count_sku -= offer
        # print(total)
        if sku in CROSS_OFFERS:
            offers = sorted(CROSS_OFFERS[sku].keys(), reverse=True)
            for offer in offers:
                if sku_counter[sku] >= offer:
                    related_items = CROSS_OFFERS[sku][offer].keys()
                    for item in related_items:
                        if item in sku_counter:
                            total -= CROSS_OFFERS[sku][offer][item] * PRICES[item]
                            sku_counter[item] -= CROSS_OFFERS[sku][offer][item]

        total += count_sku * PRICES[sku]

    return total

if __name__ == '__main__':
    # order1 = 'AAAAA'
    # assert checkout(order1) == 200
    # order2 = 'AAAAAAAA'
    # assert checkout(order2) == 330
    # order3 = 'AAAAAAAAA'
    # assert checkout(order3) == 380
    # order4 = 'AAAA'
    # assert checkout(order4) == 180
    # order5 = 'EEB'
    # assert checkout(order5) == 80
    order6 = 'EEBB'
    assert checkout(order6) == 110




from collections import Counter

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21
}

OFFERS = {
    'A': {3: 130, 5: 200},
    'B': {2: 45},
    'H': {5: 45, 10: 80},
    'K': {2: 120},
    'P': {5: 200},
    'Q': {3: 80},
    'V': {2: 90, 3: 130}
}

CROSS_OFFERS = {
    'E': {2: {'B': 1}},
    'N': {3: {'M': 1}},
    'R': {3: {'Q': 1}}
}

GET_FREE = {
    'F': {2: 1},
    'U': {3: 1}
}

BUNDLE_OFFERS = {
    ('S', 'T', 'X', 'Y', 'Z'): (3, 45)
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    sku_counter = Counter(skus)
    skus_order = []
    for sku in sku_counter:
        if sku in CROSS_OFFERS:
            skus_order.append(sku)
    skus_order.extend([sku for sku in list(sku_counter.keys()) if sku not in skus_order])
    for sku in skus_order:
        if sku not in PRICES:
            return -1
        for bundle in BUNDLE_OFFERS.keys():
            if sku in bundle:
                bundle_qty = BUNDLE_OFFERS[bundle][0]
                sub_counter = {sku: sku_counter[sku] for sku in sku_counter.keys() if sku in bundle}
                if len(sub_counter) < bundle_qty:
                    continue
                else:
                    individual_prices = list({sku: PRICES[sku] for sku in sub_counter.keys()}.values())
                    most_expensive = sorted(individual_prices, reverse=True)[:bundle_qty]
                    bundled_skus = []
                    for price in most_expensive:
                        for sub_sku in sub_counter.keys():
                            if PRICES[sub_sku] == price:
                                bundled_skus.append(sub_sku)
                                break

                    print(bundled_skus)

        if sku in GET_FREE.keys():
            offers = sorted(GET_FREE[sku].keys(), reverse=True)
            remaining = sku_counter[sku]
            for offer in offers:
                while remaining >= offer + GET_FREE[sku][offer]:
                    sku_counter[sku] -= GET_FREE[sku][offer]
                    remaining -= offer + GET_FREE[sku][offer]
        count_sku = sku_counter[sku]
        if sku in OFFERS:
            offers = sorted(OFFERS[sku].keys(), reverse=True)
            for offer in offers:
                while count_sku >= offer:
                    total += OFFERS[sku][offer]
                    count_sku -= offer
        total += count_sku * PRICES[sku]
        if sku in CROSS_OFFERS:
            remaining = sku_counter[sku]
            offers = sorted(CROSS_OFFERS[sku].keys(), reverse=True)
            for offer in offers:
                    related_items = CROSS_OFFERS[sku][offer].keys()
                    for item in related_items:
                        if item in sku_counter:
                            while remaining >= offer:
                                sku_counter[item] -= CROSS_OFFERS[sku][offer][item]
                                remaining -= offer
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
    # order6 = 'EEEEBB'
    # assert checkout(order6) == 160
    # order7 = 'BEBEEE'
    # assert checkout(order7) == 160
    # order7 = 'BEBEEEFFF'
    # assert checkout(order7) == 180
    # order8 = 'FFFFFF'
    # assert checkout(order8) == 40
    # order9 = 'FF'
    # assert checkout(order9) == 20
    # complicated_order = 'AAABBBBBCCCCDDDEEFFFGGHHHHHIIJJJNNNMUUU'
    # assert checkout(complicated_order) == 1020
    bundle_order1 = 'STXYZ'
    assert checkout(bundle_order1) == 82







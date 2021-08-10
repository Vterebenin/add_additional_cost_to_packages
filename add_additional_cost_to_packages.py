from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR


def add_additional_cost_to_packages(packs, cost):
    length = len(packs)
    if cost % length == 0:
        add_cost = cost / length
        for p in packs:
            p["price"] += add_cost
    else:
        surplus = cost % length
        add_surplus = Decimal(str(surplus)) / Decimal(str(length))
        add_cost = (Decimal(str(cost)) - Decimal(str(surplus))) / Decimal(str(length))
        add_cost += add_surplus
        flag = True
        for p in packs:
            p["price"] = Decimal(str(p["price"])) + add_cost
            if flag:
                p["price"] = p["price"].quantize(Decimal("1.00"), ROUND_CEILING)
                flag = False
            else:
                p["price"] = p["price"].quantize(Decimal("1.00"), ROUND_FLOOR)
                flag = True
    return packs


packages = [
    {"name": 'A123', "price": 10},
    {"name": 'B124', "price": 15.1},
    {"name": 'C125', "price": 40}
]
distributed_packages = add_additional_cost_to_packages(packages, 31.4)
for pa in packages:
    print(pa)

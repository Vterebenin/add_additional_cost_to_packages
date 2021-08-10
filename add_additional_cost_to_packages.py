def add_additional_cost_to_packages(packs, cost):
    length = len(packs)
    if cost % length == 0:
        add_cost = cost / length
        for p in packs:
            p["price"] += add_cost
    else:
        surplus = cost % length
        print(surplus)
        add_cost = (cost - surplus) / length
        print(add_cost)
        for p in packs:
            p["price"] += add_cost
            if surplus != 0:
                p["price"] += 1
                surplus -= 1
    return packs


packages = [
    {"name": 'A123', "price": 10},
    {"name": 'B124', "price": 15},
    {"name": 'C125', "price": 40},
    {"name": 'D126', "price": 82}
]
distributed_packages = add_additional_cost_to_packages(packages, 31)
for pa in packages:
    print(pa)
# distributed_packages is [{ name: 'A123', price: 20}, {name: 'B124', price: 25}, {name: 'C125', price: 50}]

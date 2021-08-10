def add_additional_cost_to_packages(packs, cost):
    length = len(packs)
    if cost % length == 0:
        add_cost = cost / length
        for p in packs:
            p["price"] += add_cost
    else:
        surplus = cost % length
        add_surplus = surplus / float(length)
        add_cost = float((cost - surplus)) / float(length)
        add_cost += add_surplus
        for p in packs:
            p["price"] += add_cost
    return packs


packages = [
    {"name": 'A123', "price": 10},
    {"name": 'B124', "price": 15.1},
    {"name": 'C125', "price": 40}
]
distributed_packages = add_additional_cost_to_packages(packages, 31.4)
for pa in packages:
    print("name: " + pa["name"] + " price: " + '%.2f' % pa["price"])

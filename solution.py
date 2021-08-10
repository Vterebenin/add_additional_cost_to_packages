from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR

ROUNDING = Decimal('0.01')

def round(value):
    return Decimal(value).quantize(ROUNDING)

def add_additional_cost_to_packages(packs, cost):
    if not packs or not cost:
        raise('Fill in required params')
        
    length = len(packs)
    even_cost = round(cost / length)
    leftovers = round(cost - even_cost * length)
    for pack in packs:
        pack['price'] += even_cost
    
    pack_number = 0
    while leftovers != 0:
        packs[pack_number]['price'] += ROUNDING        
        leftovers -= ROUNDING
        pack_number += 1
        if pack_number > (length - 1):
            pack_number = 1
    print(even_cost, leftovers)
    return packs


packages = [
    {"name": 'A123', "price": 0},
    {"name": 'B124', "price": 0},
    {"name": 'C124', "price": 0},
    {"name": 'D124', "price": 0},
    {"name": 'E124', "price": 0},
    {"name": 'G125', "price": 0}
]
distributed_packages = add_additional_cost_to_packages(packages, 11)
for pa in packages:
    print(pa)
    
print(sum([a['price'] for a in distributed_packages]))

def linear_search_product(products, target_product):
    indices = []
    
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    
    return indices
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target = "Apple"

result = linear_search_product(products, target)
print(result)  # Output: [0, 3, 5]


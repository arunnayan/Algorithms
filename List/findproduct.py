def find_product(list):
    currentproduct = 1
    for num in list:
        currentproduct = currentproduct* int(num)
    r = []
    for n in list:

         r.append(int(currentproduct/int(n)))

    return r


def find_product2(list):
    left = 1
    right = 1
    product = []
    for ele in list:
        product.append(left)
        left = left* ele
    print(product)
    for i in range(len(list)-1,-1,-1):
        product[i] = product[i]*right
        right= right * list[i]
    return product
print(find_product2([1,2,3]))
from collections import OrderedDict
n = int(input())
supermarket = OrderedDict()
for _ in range(n):
    item_name, space, price = input().rpartition(' ')
    price = int(price)
    supermarket[item_name] = supermarket.get(item_name, 0) + price
for item, net_price in supermarket.items():
    print(item, net_price)

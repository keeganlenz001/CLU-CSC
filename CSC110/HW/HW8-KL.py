class ItemToPurchase:
    def __init__(self, item_name, item_price, item_quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity


print('Item 1')
i1 = ItemToPurchase(input('Item name: '), float(input('Item price: ')), int(input('Item quantity: ')))
print()

print('Item 2')
i2 = ItemToPurchase(input('Item name: '), float(input('Item price: ')), int(input('Item quantity: ')))
print()

print('TOTAL COST')
print(i1.item_name, i1.item_quantity, '@', '$' + str(i1.item_price), '=',
      '$' + str(round(i1.item_price * i1.item_quantity, 2)))
print(i2.item_name, i2.item_quantity, '@', '$' + str(i2.item_price), '=',
      '$' + str(round(i2.item_price * i2.item_quantity, 2)))
print()
print('total:', '$' + str(round((i1.item_price * i1.item_quantity) + (i2.item_price * i2.item_quantity), 2)))

number_of_items = int(input("how many items? "))
prices = []
items = 0

while items != number_of_items:
    items = items + 1
    item_price = int(input("how much: $ "))
    prices.append(item_price)


print("Number of items: ", number_of_items)
for i in range(items):
    print("price of item: $", prices[i])

discount = sum(prices)
if discount >= 100:
    discount = (discount + (discount * 10)/100)
    print("total price of ", items, "items is ", discount)
else:
    print("total price of", items, "items is $", discount)

#change into for loop: for i in range of number ask again and keep adding it to the end
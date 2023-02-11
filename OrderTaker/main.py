#
with open("orders.txt", "w") as file:
    file.write("1, John Doe, Apple:5, Banana:3, Carrot:2\n")
    file.write("2, Janet Doe, Orange:10, Grape:12, Broccoli:1\n")
    file.write("3, Bob Smith, Potato:15, Onion:7, Cucumber:5\n")
    file.write("4, Enes Ozsahin, Hamburger:25\n")

# if you already have a file called orders.txt you do not need to use the first 5 lines of the code.

orders = []
with open('orders.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(',')
        order_number = int(parts[0])
        customer_name = parts[1]
        items = {}

        for item in parts[2:]:
            item_parts = item.split(':')
            items[item_parts[0].strip()] = int(item_parts[1].strip())

        order = {
            'Order Number': order_number,
            'Customer': customer_name,
            'Items': items
        }
        orders.append(order)

print(orders)

class UberEats:
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address
        self.add_shop = {}
        self.price = 0
        print(f"{self.name} Welcome to UberEats!")

    def add_items(self, item1, item2, item1_price, item2_price):
        self.add_shop = {item1: item1_price, item2: item2_price}
        self.price = item1_price + item2_price

    def print_order_detail(self):
        result = f"User details: Name: {self.name}, Phone:\n{self.number}, Address: {self.address} Orders: {self.add_shop}\nTotal Paid Amount: {self.price} "

        return result


order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())


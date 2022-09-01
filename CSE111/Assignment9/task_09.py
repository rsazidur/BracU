class Fruit:
    Total_order=0
    
    def __init__(self, Order_ID, weight):
        self.Order_ID=Order_ID
        self.weight=weight
        Fruit.Total_order=Fruit.Total_order+1
    
    def __str__(self):
        return self.Order_ID+", Weight: "+str(self.weight)

class Mango(Fruit):
     #write your code here
    def __init__(self, oder_id, weight, name, price_kg):
        super().__init__(oder_id, weight)
        self.name = name
        self.price_kg = price_kg

    def __str__(self):
        return f"{super().__str__()}, Variety: {self.name}, Total Price: {self.weight * self.price_kg}"

    def __add__(self, other):
        return f"The total Price of the orders are: {(self.weight * self.price_kg) + (other.weight * other.price_kg)}"
     

class JackFruit(Fruit):
      #write your code here

    def __init__(self, oder_id, weight, price_kg):
        super().__init__(oder_id, weight)
        self.price_kg = price_kg

    def __str__(self):
        return f"{super().__str__()}, Total Price: {self.weight * self.price_kg}"

    def __add__(self, other):
        return f"The total Price of the orders are: {(self.weight * self.price_kg) + (other.weight * other.price_kg)}"
    
m1=Mango("Order Id 1", 5,"GopalVog",250)
print(m1)
m2=Mango("Order Id 2", 5,"HariVanga", 230)
print(m2) 
j1=JackFruit("Order Id 3", 5,250)
print(j1)
j2=JackFruit("Order Id 4", 4,210)
print(j2)
print("Total number of Orders: "+str(Fruit.Total_order))
print("==================")
print(m1+m2)
print("==================")
print(j1+j2)

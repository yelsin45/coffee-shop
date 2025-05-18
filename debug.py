from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
mocha = Coffee("Mocha")

# Orders
order1 = alice.create_order(latte, 4.5)
order2 = alice.create_order(mocha, 5.0)
order3 = bob.create_order(latte, 5.5)

# Test relationships
print(alice.orders())          # [order1, order2]
print(bob.coffees())           # [latte]
print(latte.customers())       # [alice, bob]
print(latte.num_orders())      # 2
print(latte.average_price())   # 5.0
print(Customer.most_aficionado(latte))  # bob (spent 5.5)
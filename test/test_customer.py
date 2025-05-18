import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("x" * 16)
    with pytest.raises(TypeError):
        Customer(123)

def test_customer_orders_and_coffees():
    c = Customer("Test")
    coffee = Coffee("Espresso")
    c.create_order(coffee, 2.5)
    assert coffee in c.coffees()
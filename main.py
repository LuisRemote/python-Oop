from item import Item
from phone import Phone
from keyboard import Keyboard


# Encapsulation

# item1 = Item("MyItem", 750)
# item1.apply_increment(0.2)
# item1.apply_discount()
# Getting an Attibute
# print(item1.price)


# Abstraction

# item1 = Item("MyItem", 750, 6)
# item1.send_email()


# Inheritance

# item1 = Phone("rwPhone", 1000, 3)
# item1.apply_increment(0.2)
# print(item1.price)


# Polymorphism

item1 = Keyboard("rwKeyboard", 1000, 3)
item1.apply_discount()

print(item1.price)

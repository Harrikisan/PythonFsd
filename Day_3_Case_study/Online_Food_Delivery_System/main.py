from food_item import FoodItem
from user import User
from premium_user import PremiumUser

pizza = FoodItem("Pizza", 250)
burger = FoodItem("Burger", 150)
pasta = FoodItem("Pasta", 200, available=False)
fries = FoodItem("Fries", 100)

harri = User("Harri")
kisan = PremiumUser("Kisan")

harri.order.add_item(pizza)
harri.order.add_item(burger)
harri.order.add_item(pasta)
harri.order.display_order()
harri.display_total()

print("\n---\n")

kisan.order.add_item(pizza)
kisan.order.add_item(fries)
kisan.order.remove_item("Fries")
kisan.order.display_order()
kisan.display_total()

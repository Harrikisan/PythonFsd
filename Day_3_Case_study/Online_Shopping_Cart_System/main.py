from product import Product
from user import User
from premium_user import PremiumUser

def main():
    laptop = Product("Laptop", 1000, 5)
    mouse = Product("Mouse", 50, 10)
    keyboard = Product("Keyboard", 80, 7)

    print("\nAvailable Products:")
    laptop.display_info()
    mouse.display_info()
    keyboard.display_info()

    harri = User("Harri")
    kisan = PremiumUser("Kisan")

    harri.add_to_cart(laptop, 1)
    harri.add_to_cart(mouse, 2)
    harri.view_cart()
    harri.calculate_total()

    kisan.add_to_cart(laptop, 1)
    kisan.add_to_cart(keyboard, 1)
    kisan.view_cart()
    kisan.calculate_total()

    harri.remove_from_cart(mouse, 1)
    harri.view_cart()
    harri.calculate_total()

    print("\nFinal Stock Status:")
    laptop.display_info()
    mouse.display_info()
    keyboard.display_info()

if __name__ == "__main__":
    main()

import os
from datetime import datetime

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} - Qty: {self.quantity}"


class POSSystem:
    def __init__(self):
        # Determine paths relative to this script
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.products_file = os.path.join(self.base_dir, "products.txt")
        self.sales_file = os.path.join(self.base_dir, "sales.txt")
        
        self.products = []
        self.cart = {}  # Store as: {product_name: quantity}
        
        # Load products on initialization
        self.load_products()

    def load_products(self):
        """Loads products from the products.txt file. 
        Creates the file with some default products if it does not exist."""
        self.products = []
        if not os.path.exists(self.products_file):
            # Pre-populate with some default products for easy testing
            default_products = [
                Product("Rice", 10.0, 10),
                Product("Sugar", 5.0, 20),
                Product("Milk", 4.0, 15)
            ]
            self.products = default_products
            self.save_products()
            return

        try:
            with open(self.products_file, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(',')
                    if len(parts) == 3:
                        name, price, qty = parts
                        self.products.append(Product(name, float(price), int(qty)))
        except Exception as e:
            print(f"Error loading products: {e}")

    def save_products(self):
        """Saves the current product list to products.txt."""
        try:
            with open(self.products_file, 'w') as file:
                for product in self.products:
                    file.write(f"{product.name},{product.price},{product.quantity}\n")
        except Exception as e:
            print(f"Error saving products: {e}")

    def add_product(self):
        """Allows cashier to add a new product or update inventory for an existing product."""
        print("\n=== Add Product ===")
        name = input("Enter product name: ").strip()
        if not name:
            print("Product name cannot be empty.")
            return

        # Check if product already exists
        for p in self.products:
            if p.name.lower() == name.lower():
                print(f"Product '{p.name}' already exists.")
                # Allow updating stock using try/except
                while True:
                    try:
                        qty_input = input(f"Enter additional quantity to add to stock (Current: {p.quantity}): ")
                        qty_to_add = int(qty_input)
                        if qty_to_add < 0:
                            print("Quantity cannot be negative.")
                            continue
                        p.quantity += qty_to_add
                        self.save_products()
                        print(f"Successfully added stock. New stock for '{p.name}' is {p.quantity}.")
                        return
                    except ValueError:
                        print("Invalid number")

        # Get price with validation
        price = 0.0
        while True:
            try:
                price_input = input("Enter price: ")
                price = float(price_input)
                if price < 0:
                    print("Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid number")

        # Get quantity with validation
        quantity = 0
        while True:
            try:
                qty_input = input("Enter quantity: ")
                quantity = int(qty_input)
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid number")

        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        self.save_products()
        print(f"Product '{name}' added successfully!")

    def show_products(self):
        """Displays all available products and their stock."""
        print("\n=== Show Products ===")
        if not self.products:
            print("No products available.")
            return

        for index, product in enumerate(self.products, 1):
            print(f"{index}. {product.name} - ${product.price:.2f} (Qty: {product.quantity})")

    def add_to_cart(self):
        """Adds a specified quantity of an available product to the cart."""
        print("\n=== Add To Cart ===")
        if not self.products:
            print("No products available to buy.")
            return

        self.show_products()
        
        # Product selection
        choice = 0
        while True:
            try:
                choice_input = input("\nEnter product number to add to cart (or 0 to cancel): ")
                choice = int(choice_input)
                if choice == 0:
                    return
                if 1 <= choice <= len(self.products):
                    break
                else:
                    print(f"Please select a number between 1 and {len(self.products)}.")
            except ValueError:
                print("Invalid number")

        selected_product = self.products[choice - 1]

        if selected_product.quantity == 0:
            print(f"Sorry, '{selected_product.name}' is out of stock.")
            return

        # Quantity selection
        qty = 0
        while True:
            try:
                qty_input = input(f"Enter quantity of '{selected_product.name}' to add (Max {selected_product.quantity}): ")
                qty = int(qty_input)
                if qty <= 0:
                    print("Quantity must be greater than 0.")
                    continue
                if qty > selected_product.quantity:
                    print(f"Insufficient stock. Only {selected_product.quantity} units available.")
                    continue
                break
            except ValueError:
                print("Invalid number")

        # Check total cart quantity does not exceed stock
        current_cart_qty = self.cart.get(selected_product.name, 0)
        if current_cart_qty + qty > selected_product.quantity:
            print(f"Cannot add {qty} more. Total in cart ({current_cart_qty + qty}) would exceed stock ({selected_product.quantity}).")
            return

        self.cart[selected_product.name] = current_cart_qty + qty
        print(f"Added {qty} x '{selected_product.name}' to cart.")

    def checkout(self):
        """Processes checkout, calculates total, updates inventory, and saves receipt to sales.txt."""
        print("\n=== Checkout ===")
        if not self.cart:
            print("Your cart is empty. Add items to cart first.")
            return

        total_bill = 0.0
        receipt_lines = []

        # List items in cart and calculate prices
        for item_name, qty in self.cart.items():
            product = next((p for p in self.products if p.name == item_name), None)
            if product:
                item_total = product.price * qty
                total_bill += item_total
                line = f"{product.name} - Qty: {qty} @ ${product.price:.2f} = ${item_total:.2f}"
                print(line)
                receipt_lines.append(line)
                # Deduct inventory stock
                product.quantity -= qty

        print(f"Total = ${total_bill:.2f}")
        print("=================")

        # Save receipt to sales.txt
        try:
            with open(self.sales_file, 'a') as file:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"\nReceipt - {timestamp}\n")
                for line in receipt_lines:
                    file.write(f"  {line}\n")
                file.write(f"Total = ${total_bill:.2f}\n")
                file.write("-" * 40 + "\n")
            print(f"Receipt successfully saved to sales.txt")
        except Exception as e:
            print(f"Error saving receipt: {e}")

        # Save updated stock to products file
        self.save_products()

        # Clear cart
        self.cart.clear()
        print("Checkout completed!")

    def run(self):
        """Runs the main menu loop of the POS system."""
        while True:
            print("\n=== POS System Menu ===")
            print("1. Add Product")
            print("2. Show Products")
            print("3. Add To Cart")
            print("4. Checkout")
            print("5. Exit")
            print("=======================")
            
            choice = input("Enter choice (1-5): ").strip()
            
            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.show_products()
            elif choice == '3':
                self.add_to_cart()
            elif choice == '4':
                self.checkout()
            elif choice == '5':
                print("Thank you for using Simple POS System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    pos = POSSystem()
    pos.run()

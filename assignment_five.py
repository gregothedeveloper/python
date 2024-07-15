import csv
import os

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
    
    def __str__(self):
        return f"Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

def read_products_from_file(filename):
    products = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                name, price, quantity = row
                products.append(Product(name, price, quantity))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print(f"Error: Incorrect data format in '{filename}'.")
    
    return products

def write_products_to_file(filename, products):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for product in products:
                writer.writerow([product.name, product.price, product.quantity])
    except IOError:
        print(f"Error: Unable to write to file '{filename}'.")

def display_products(products):
    if not products:
        print("No products found.")
    else:
        for index, product in enumerate(products, start=1):
            print(f"{index}. {product}")

def add_product(products):
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    quantity = input("Enter product quantity: ")
    products.append(Product(name, price, quantity))
    print("Product added successfully.")

def update_product(products):
    display_products(products)
    try:
        index = int(input("Enter the index of the product to update: ")) - 1
        if 0 <= index < len(products):
            name = input("Enter updated product name: ")
            price = input("Enter updated product price: ")
            quantity = input("Enter updated product quantity: ")
            products[index] = Product(name, price, quantity)
            print("Product updated successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_product(products):
    display_products(products)
    try:
        index = int(input("Enter the index of the product to delete: ")) - 1
        if 0 <= index < len(products):
            del products[index]
            print("Product deleted successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    filename = "products.csv"
    products = read_products_from_file(filename)

    while True:
        print("\n===== Product Management System =====")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_products(products)
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            update_product(products)
        elif choice == '4':
            delete_product(products)
        elif choice == '5':
            write_products_to_file(filename, products)
            print("Exiting program. Changes saved to 'products.csv'.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
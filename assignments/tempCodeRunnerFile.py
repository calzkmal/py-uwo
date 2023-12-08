class Product:
    def __init__(self, name, price, category):
        # Initialize product attributes
        self._name = name
        self._price = price
        self._category = category

    # Define how products are classified
    def __eq__(self, other): 
         if isinstance(other, Product):
             if  ((self._name == other._name and self._price == other._price) and (self._category==other._category)):
                return True
             else:
                return False
         else:
            return False

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_category(self):
        return self._category

    # Implement string representation
    def __repr__(self):
        rep = 'Product(' + self._name + ',' + str(self._price) + ',' + self._category + ')'
        return rep

class Inventory:
    def __init__(self):
        self._inventory_data = {}
    
    def add_to_productInventory(self, productName, productPrice, productQuantity):
        self._inventory_data[productName] = {
            'price': productPrice,
            'quantity': productQuantity
        }
    
    def add_productQuantity(self, nameProduct, addQuantity):
        if nameProduct in self._inventory_data:
            self._inventory_data[nameProduct]['quantity'] += addQuantity
    
    def remove_productQuantity(self, nameProduct, removeQuantity):
        if nameProduct in self._inventory_data:
            self._inventory_data[nameProduct]['quantity'] -= removeQuantity
    
    def get_productPrice(self, nameProduct):
        return self._inventory_data[nameProduct]['price']
    
    def get_productQuantity(self, nameProduct):
        return self._inventory_data[nameProduct]['quantity']
    
    def display_inventory(self):
        for products, info in self._inventory_data.items():
            print(f"{products}, {info['price']}, {info['quantity']}")

class ShoppingCart:
    def __init__(self, buyerName, inventory):
        self._buyerName = buyerName
        self._inventory = inventory
        self._cart = {}
    
    def add_to_cart(self, nameProduct, requestedQuantity):
        if nameProduct not in self._cart:
            self._cart[nameProduct] = 0
        
        availableQuantity = self._inventory.get_productQuantity(nameProduct)
        if requestedQuantity > availableQuantity:
            return "Can not fill the order"
        
        self._cart[nameProduct] += requestedQuantity
        self._inventory.remove_productQuantity(nameProduct, requestedQuantity)
        return "Filled the order"

    def remove_from_cart(self, nameProduct, requestedQuantity):
        if nameProduct not in self._cart:
            return "Product not in the cart"

        cartQuantity = self._cart[nameProduct]

        if requestedQuantity > cartQuantity:
            return "The requested quantity to be removed from cart exceeds what is in the cart"

        result = self._inventory.remove_productQuantity(nameProduct, requestedQuantity)

        if result == "Successful":
            self._cart[nameProduct] -= requestedQuantity
            if self._cart[nameProduct] == 0:
                del self._cart[nameProduct]
            return "Successful"
        else:
            return "Failed to remove item from the cart"

    def view_cart(self):
        total_price = 0
        for product, quantity in self._cart.items():
            price = self._inventory.get_productPrice(product)
            total_price += price * quantity
            print(f"{product} {quantity}")

        print(f"Total: {total_price}")
        print(f"Buyer Name: {self._buyerName}")  


inventory = Inventory()
inventory.add_to_productInventory("Backpack", 60, 100)
inventory.add_to_productInventory("Frying pan", 80, 200)
inventory.add_to_productInventory("Intro to Python", 90, 1000)
inventory.add_to_productInventory("Diamond", 10000, 20)

shopping_cart = ShoppingCart("Jane Doe", inventory)

# Example usage
result = shopping_cart.add_to_cart("Backpack", 5)
print(result)

result = shopping_cart.remove_from_cart("Backpack", 3)
print(result)

shopping_cart.view_cart()

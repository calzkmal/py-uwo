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


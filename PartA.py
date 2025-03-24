# PartA.py
# So this is my Part A code for the test. I chose "Phone" with attributes:
# brand, model, year, price, and colour.

class Phone:
    def __init__(self, brand, model, year, price, colour):
        # Checking the data types here just to be safe.
        if not isinstance(brand, str):
            raise TypeError("brand must be a string")
        if not isinstance(model, str):
            raise TypeError("model must be a string")
        if not isinstance(year, int):
            raise TypeError("year must be an integer")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if not isinstance(colour, str):
            raise TypeError("colour must be a string")
        
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour

    def print_attributes(self):
        print(f"Phone Attributes:\n Brand: {self.brand}\n Model: {self.model}\n Year: {self.year}\n Price: {self.price}\n Colour: {self.colour}")

    # Methods to update each attribute, making sure types are still correct.
    def update_brand(self, new_brand):
        if isinstance(new_brand, str):
            self.brand = new_brand
        else:
            raise TypeError("brand must be a string")

    def update_model(self, new_model):
        if isinstance(new_model, str):
            self.model = new_model
        else:
            raise TypeError("model must be a string")

    def update_year(self, new_year):
        if isinstance(new_year, int):
            self.year = new_year
        else:
            raise TypeError("year must be an integer")

    def update_price(self, new_price):
        if isinstance(new_price, (int, float)):
            self.price = new_price
        else:
            raise TypeError("price must be a number")

    def update_colour(self, new_colour):
        if isinstance(new_colour, str):
            self.colour = new_colour
        else:
            raise TypeError("colour must be a string")


# Child class: Smartphone (has its own extra attributes).
class Smartphone(Phone):
    def __init__(self, brand, model, year, price, colour, operating_system, storage_capacity):
        super().__init__(brand, model, year, price, colour)
        # Extra attributes for smartphones.
        if not isinstance(operating_system, str):
            raise TypeError("operating_system must be a string")
        if not isinstance(storage_capacity, (int, float)):
            raise TypeError("storage_capacity must be a number")
        self.operating_system = operating_system
        self.storage_capacity = storage_capacity  # in GB

    def print_extra_attributes(self):
        print(f"Smartphone Extra Attributes:\n Operating System: {self.operating_system}\n Storage Capacity: {self.storage_capacity}GB")

    def print_all_attributes(self):
        # Just reusing print_attributes and then adding my own.
        self.print_attributes()
        self.print_extra_attributes()

    # Update methods for these extra attributes.
    def update_operating_system(self, new_os):
        if isinstance(new_os, str):
            self.operating_system = new_os
        else:
            raise TypeError("operating_system must be a string")

    def update_storage_capacity(self, new_storage):
        if isinstance(new_storage, (int, float)):
            self.storage_capacity = new_storage
        else:
            raise TypeError("storage_capacity must be a number")


# Quick demo of how it all works.
if __name__ == "__main__":
    print("=== Creating Instances ===")
    # Here’s the Phone instance.
    phone_instance = Phone("Apple", "iPhone 13", 2021, 799.99, "Black")
    phone_instance.print_attributes()
    
    # Here’s the Smartphone instance.
    smartphone_instance = Smartphone("Samsung", "Galaxy S21", 2021, 699.99, "White", "Android", 128)
    smartphone_instance.print_all_attributes()
    
    print("\n=== Updating Attributes ===")
    # Updating the base class (do it twice to show it works).
    phone_instance.update_brand("Apple Inc.")
    phone_instance.update_year(2022)
    print("After update (Phone):")
    phone_instance.print_attributes()
    
    # Updating the child class (also doing it twice).
    smartphone_instance.update_operating_system("Android 12")
    smartphone_instance.update_storage_capacity(256)
    print("After update (Smartphone):")
    smartphone_instance.print_all_attributes()

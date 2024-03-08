####
# Products for product factory
# - CLY 040324 -
####
####
# Added an automated id
# - CLY 050324 -
####

class Item:
    # Id of latest item, whenever an item is created a new unique id is given to the item.
    latest_id = 0
    def __init__(self, name, price, description):
        Item.latest_id += 1
        self.id = Item.latest_id
        self.name = name
        self.price = price
        self.description = description

    def display_info(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Description:", self.description)

class Laptop(Item):
    latest_id = 0
    def __init__(self, name, price, description, brand, processor, gpu, os):
        Laptop.latest_id += 1
        self.id = Laptop.latest_id
        super().__init__(name, price, description)
        self.brand = brand
        self.processor = processor
        self.os = os
        self.gpu = gpu

    def display_info(self):
        super().display_info()
        print("Brand:", self.brand)
        print("Processor:", self.processor)

class Charger(Item):
    latest_id = 0
    def __init__(self, name, price, description, brand, charge):
        Charger.latest_id += 1
        self.id = Charger.latest_id
        super().__init__(name, price, description)
        self.brand = brand
        self.charge = charge

    def display_info(self):
        super().display_info()
        print("Brand:", self.brand)
        print("Charge in Watts:", self.charge)

class Monitor(Item):
    latest_id = 0
    def __init__(self, name, price, description, monitor_size):
        self.id = Monitor.latest_id
        super().__init__(name, price, description)
        self.monitor_size = monitor_size

class Desktop(Item):
    latest_id = 0
    def __init__(self, name, price, description, gpu, brand, processor, os):
        self.id = Desktop.latest_id
        super().__init__(name, price, description)
        self.gpu = gpu
        self.brand = brand
        self.processor = processor
        self.os = os
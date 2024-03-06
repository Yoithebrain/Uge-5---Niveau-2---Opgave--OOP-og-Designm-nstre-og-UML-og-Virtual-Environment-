import importlib
import Item
###
# My product factory to create specific products within the item class
# - CLY 040324 -
###
class ProductFactory:
    # Method to create a new item
    @classmethod
    def create_item(cls, item_type, *args, **kwargs):
        item_class = cls._load_class(item_type)
        if item_class:
            return item_class(*args, **kwargs)
        else:
            raise ValueError("Invalid item type")
    # Method to load the class from within the Item module
    @staticmethod
    def _load_class(item_type):
        try:
            module_name = Item.__name__  # Module name where the classes are defined
            module = importlib.import_module(module_name)
            item_class = getattr(module, item_type)
            print("Item type:", item_type)
            print("Item class:", item_class)
            if item_class:
                return item_class
        except AttributeError as e:
            print(f"An error occurred while trying to load the item for the class: {e}")
            pass
        return None
# Debug laptop - Use this to test the class on its own
#laptop = ProductFactory.create_item("Laptop", "Laptop", 1000.99, "'High-performance' laptop, very good in current year we promise", "ShitWarez", "Intel Core i3", "GTX 750 TX", "Linux Ubuntu")
#laptop.display_info()
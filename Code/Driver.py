# Imports
import ProductFactory
from Database import Database as db

class Driver:
    # Initilization of driver class
    def __init__(self):
        self.db = db()
    
    def run(self):
        # Create products and add them to the database
        factory = ProductFactory.ProductFactory()
        # Example of creating an item:
        '''
        laptop = ProductFactory.create_item("Laptop", "Laptop", 1000.99, 
        "'High-performance' laptop, very good in current year we promise", "BadWarez", "Intel Core i3", "GTX 750 TX", 
        "Linux Ubuntu")
        '''
        monitor = factory.create_item("Monitor", "Samsung Monitor", 1500, "40 inch Samsun monitor", 40)
        # A quick print before adding the information to the database
        monitor.display_info()
        # Database is a dict. object to showcase the idea of a singleton database connection
        self.db.insert_data("monitor", monitor)
        # Test insert
        self.db.insert_data("key2", "test value")

        # load monitor data
        monitor_data = self.db.get_data('monitor')
        monitor_data.display_info()

        # Make a new instance to load the same monitor to showcase that the Db object is singleton
        my_database_2 = db()
        monitor_data = my_database_2.get_data('monitor')
        monitor_data.display_info()

# Example usage:
if __name__ == "__main__":
    driver = Driver()
    driver.run()

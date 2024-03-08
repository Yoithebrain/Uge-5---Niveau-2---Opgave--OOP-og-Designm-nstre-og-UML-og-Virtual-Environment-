###
# Database class - makes use of a dictionary to contain the items for now
# - CLY 030824 -
####
# Imports
import logging

# Logging configuration
logging.basicConfig(filename='database.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Logging decorator
def log_action(func):
    def wrapper(*args, **kwargs):
        # Calls the original method
        result = func(*args, **kwargs)
        # Get the name of the action performed
        action = func.__name__
        # Log the action, key and value into the log file
        if action == 'insert_data':
            key, value = args[0], args[1]
            logging.info(f"Item added: Key='{key}', Value='{value}'")
        elif action == 'get_data':
            key = args[0]
            value = result
            logging.info(f"Item loaded: Key='{key}', Value='{value}'")
        elif action == 'delete_data':
            key = args[0]
            logging.info(f"Item deleted: Key='{key}'")
        return result
    return wrapper
# Class definition
class Database:
    _instance = None
    _data = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    @staticmethod
    @log_action
    def insert_data(key, value):
        Database._data[key] = value
    @staticmethod
    @log_action
    def get_data(key):
        return Database._data.get(key)
    @staticmethod
    @log_action
    def delete_data(key):
        if key in Database._data:
            del Database._data[key]

# Debug code - Example usage:

db1 = Database()
db1.insert_data("key1", "value1")

db2 = Database()  # Same instance as db1
print(db2.get_data("key1"))  # Output: value1

db2.insert_data("key2", "value2")
print(db1.get_data("key2"))  # Output: value2 (Both instances share the same data)

db1.delete_data("key1")
print(db2.get_data("key1"))  # Output: None (Changes made in one instance affect the other)

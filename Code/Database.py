class Database:
    _instance = None
    _data = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def insert_data(self, key, value):
        self._data[key] = value

    def get_data(self, key):
        return self._data.get(key)

    def delete_data(self, key):
        if key in self._data:
            del self._data[key]

# Debug code:
'''
db1 = Database()
db1.insert_data("key1", "value1")

db2 = Database()  # Same instance as db1
print(db2.get_data("key1"))  # Output: value1

db2.insert_data("key2", "value2")
print(db1.get_data("key2"))  # Output: value2 (Both instances share the same data)

db1.delete_data("key1")
print(db2.get_data("key1"))  # Output: None (Changes made in one instance affect the other)
'''
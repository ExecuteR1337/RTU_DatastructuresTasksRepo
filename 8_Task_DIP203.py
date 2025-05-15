class HashTable:

    def __init__(self, size=4):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        i = self._hash(key)
        while self.table[i] and self.table[i][0] != key:
            i = (i + 1) % self.size
        self.table[i] = (key, value)

    def get(self, key):
        i = self._hash(key)
        while self.table[i]:
            if self.table[i][0] == key: return self.table[i][1]
            i = (i + 1) % self.size
        return None

    def print_table(self):
        for i, item in enumerate(self.table):
            print(f"{i}: {item}")

h = HashTable()
h.insert("Toyota", 1)
h.insert("Nissan", 2)
h.insert("Mitsubishi", 3)
h.insert("Honda", 4)
h.print_table()
target = h.get("Mitsubishi")
print(f"\nTarget points to: {target}") # By B. Nazarzoda 241ADB013
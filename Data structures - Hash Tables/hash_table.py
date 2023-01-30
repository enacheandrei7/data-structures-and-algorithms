"""
Implementation of hash tables in python
"""

class HashTable():
    """Class for implementing Hash Table data structure in Python"""
    def __init__(self, size) -> None:
        self.size = size
        self.data = [[] for i in range(self.size)]


    def __str__(self):
        return str(self.__dict__)


    def hash(self, key):
        """Hashes the data from key"""
        hashed_val = 0
        for idx, char in enumerate(key):
            hashed_val += ord(char) * (idx + 1)
        return hashed_val % self.size


    # def add(self, key, value):
    def __setitem__(self, key, value): #  __setitem__ lets us use method for pushing info like a dict a['x'] = 5
        """Adds element to the hash table"""
        address = self.hash(key)
        found = False

        # We check if the data is already in the linked list stored in the hash table
        for idx, elem in enumerate(self.data[address]):
            if len(elem) == 2 and elem[0] == key:
                self.data[address][idx] = (key, value)
                found = True
                break
        if not found:
            self.data[address].append((key, value))


    # def get(self, key):
    def __getitem__(self, key): #  __getitem__ lets us use method for retrieveing info like a dict a['x']
        """Retrieves the element with the key key from hash table"""
        hashed_val = self.hash(key)
        for elem in self.data[hashed_val]:
            if elem[0] == key:
                return elem[1]

    def __delitem__(self, key):
        """Deletes element with key from hash table"""
        hashed_val = self.hash(key)
        for idx, kv in enumerate(self.data[hashed_val]):
            if kv[0] == key:
                del self.data[hashed_val][idx]



t = HashTable(10)
print('Hashed values for some keys:')
print(t.hash('Alex'))
print(t.hash('march 6'))
print(t.hash('march 9'))
# t.add('Andrei En', 100)
# print(t.get('Andrei En'))
t['Alex'] = 100
t['march 6'] = 22
t['june 17'] = 11
print('Initial populated hash table:\n', t)
t['march 9'] = 11
print("The value for the key 'Alex': ", t['Alex'])
print(t)
t['march 9'] = 22
t['june 17'] = 999
print(t['june 17'])
del t['march 6']
print("Hash table after modifying 'march 9' and deleting 'march 6':\n", t)

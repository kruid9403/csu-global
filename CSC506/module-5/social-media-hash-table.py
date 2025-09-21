class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size
    
    def set(self, key, value):
        idx = self.hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[idx].append([key,value])

    def get(self, key):
        idx = self.hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def remove(self, key):
        idx = self.hash(key)
        for pair in self.table[idx]:
            if pair [0] == key:
                pair[1] = None
                return
    
if __name__ == "__main__":
    ht = HashTable(10)
    ht.set("Alice", ["post 1", "post 2"])
    print("Alices recs = ", ht.get("Alice"))
    ht.set("Alice", ["post 6", "post7"])
    print("Alices updated recs = ", ht.get("Alice"))
    print("Carols recs = (None)", ht.get("Carol"))
    ht.set("Carol", ["post 9", "post 0"])
    print("Carols recs = ", ht.get("Carol"))
    ht.remove("Carol")
    print("Carols removed recs (None Again)", ht.get("Carol"))
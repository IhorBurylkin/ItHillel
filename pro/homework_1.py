class SomeDict:
    def __init__(self, capacity=8, load_factor_threshold=0.7):
        self.capacity = capacity        
        self.size = 0                   
        self.load_factor_threshold = load_factor_threshold
        self.table = [None] * self.capacity  

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_table = self.table
        self.capacity *= 2                
        self.table = [None] * self.capacity
        self.size = 0                    

        for item in old_table:
            if item is not None:
                key, value = item
                self[key] = value

    def __setitem__(self, key, value):
        if self.size / self.capacity >= self.load_factor_threshold:
            self._resize()
        
        index = self._hash(key)
        while self.table[index] is not None:
            existing_key, _ = self.table[index]
            if existing_key == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.capacity

        self.table[index] = (key, value)
        self.size += 1

    def __getitem__(self, key):
        index = self._hash(key)
        start_index = index

        while self.table[index] is not None:
            existing_key, value = self.table[index]
            if existing_key == key:
                return value
            index = (index + 1) % self.capacity
            if index == start_index:
                break
        raise KeyError(f"Key {key} not found.")

    def __str__(self):
        pairs = []
        for item in self.table:
            if item is not None:
                pairs.append(f"{item[0]}: {item[1]}")
        return "{" + ", ".join(pairs) + "}"

    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except KeyError:
            return False

some_dict = SomeDict()

# Наявність у класса варіації хеш-таблиці
print(hasattr(SomeDict, '_hash'))

# Додавання нової пари ключ:значення
print("Поточний словник:", some_dict)
some_dict["digit"] = 10
some_dict["word"] = "word"
some_dict["list"] = [1, 2, 3]
print("Словник пiсля додавання значень:", some_dict)

# Вставка нової пари в правльне місце хеш-таблиці через обчислення індексу
some_dict["digit"] = 15
print("digit:", some_dict["digit"])

# Отримання значення за ключем
print("word:", some_dict["word"])

# Маштабування хеш-таблиці
for i in range(20):
    some_dict[f"key{i}"] = i
print("Словник після масштабування:", some_dict)
import random


class RandomizedSet:
    def __init__(self):
        self.vals = []
        self.val_map = dict()

    def insert(self, val: int) -> bool:
        if val in self.val_map:
            return False
        self.val_map[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_map:
            return False

        index = self.val_map[val]
        last_index = len(self.vals) - 1
        last_val = self.vals[last_index]
        self.vals[index], self.vals[last_index] = self.vals[last_index], self.vals[index]
        self.val_map[last_val] = index
        self.val_map.pop(val)
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)

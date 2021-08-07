class MyHashMap:
    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        return self.map[key]

    def remove(self, key: int) -> None:
        if key in self.map:
            del self.map[key]

class KeyNode:
    def __init__(self, key, val = None):
        self.key = key
        self.val = val

    def __repr__(self):
        return f"KeyNode(key: {self.key}, val: {self.val})"


class MyHashMapKeyNode:
    def __init__(self):
        self.key_range = 769
        self.hash_table = [[] for _ in range(self.key_range)]

    def _get_bucket(self, key: int):
        return self.hash_table[key % self.key_range]

    def put(self, key: int, value: int) -> None:
        bucket = self._get_bucket(key)
        for node in bucket:
            if node.key == key:
                node.val = value
                return
        bucket.append(KeyNode(key, value))

    def get(self, key: int) -> int:
        bucket = self._get_bucket(key)
        for node in bucket:
            if node.key == key:
                return node.val
        return -1

    def remove(self, key: int) -> None:
        bucket = self._get_bucket(key)
        for index, node in enumerate(bucket):
            if node.key == key:
                bucket.pop(index)
                return


class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key: int):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key:int, value: int):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[i] = (key, value)
                return

        self.bucket.append((key, value))

    def delete(self, key: int):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket.pop(i)


class MyHashMapTuple:
    def __init__(self):
        self.key_range = 769
        self.hash_table = [Bucket() for _ in range(self.key_range)]

    def _get_bucket(self, key: int):
        return self.hash_table[key % self.key_range]

    def put(self, key: int, value: int) -> None:
        bucket = self._get_bucket(key)
        bucket.update(key, value)

    def get(self, key: int) -> int:
        bucket = self._get_bucket(key)
        return bucket.get(key)

    def remove(self, key: int) -> None:
        bucket = self._get_bucket(key)
        bucket.delete(key)
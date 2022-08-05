'''

select * from table_name where  table_name.dob
LRU Cache Implement the LRUCache   class:   LRUCache(int capacity)
Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.Otherwise, add the key - value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict  the least recently used key.
The functions get and put must each run in O(1) average time complexity.


Example
1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

1,2
3,1,2
2,3,1
4,2,3

3,2,1
2,3,1
4,2,3

get & put - move element to 0th position

Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

'''

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # self.data = OrderedDict()
        self.data = []

    def get(self, key: int) -> int:

        if key in self.data:
            idx = self.data.index(key)
            if idx == 0:
                pass
            else:
                self.data.remove(key)
                self.data.insert(0, key)
            #print(self.data)
            return key
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.data) < self.capacity:
            if key not in self.data:
                self.data.insert(0, key)

        else:
            self.data.pop(-1)
            self.data.insert(0, key)
        #print(self.data)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(3)
obj.put(1, 1)
obj.put(2, 2)
p = obj.get(1)
print(f'{p}')
obj.put(3, 3)

v = obj.get(2)
print(f'{v}')
obj.put(4, 4)
r = obj.get(1)
print(r)
s = obj.get(3)
print(s)
t = obj.get(4)
print(t)

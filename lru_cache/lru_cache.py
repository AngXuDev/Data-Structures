from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.storage = DoublyLinkedList()
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.cache:
            # self.storage.delete(self.storage.get_node(key))
            # self.storage.add_to_tail(key)
            self.storage.move_to_end(self.storage.get_node(key))
            # _, node = self.cache[key]
            # self.storage.move_to_end(node)
            return self.cache.get(key, None)
        print("self.cache :", self.cache)

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            # self.storage.delete(self.storage.get_node(key))
            # self.storage.add_to_tail(key)
            # _, node = self.cache[key]
            # self.storage.move_to_end(node)
            self.storage.move_to_end(self.storage.get_node(key))
        elif len(self.storage) < self.limit:
            self.storage.add_to_tail(key)
            self.cache[key] = value
        elif len(self.storage) >= self.limit:
            self.cache.pop(self.storage.remove_from_head(), None)
            self.storage.add_to_tail(key)
            self.cache[key] = value
        print("self.cache :", self.cache)

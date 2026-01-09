class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):

        # initialise the map
        self.__capacity = capacity
        self.__map: dict[(int, int), Node] = {}

        # initialise the doubly linked list
        self.__head = Node()
        self.__tail = Node()
        self.__head.next = self.__tail
        self.__tail.prev = self.__head

    # on each get, we move node to the end of the list
    def get(self, key: int) -> int:
        if key in self.__map:

            val = self.__map[key].val[1]

            # move from the middle to the tail
            node = self.__map[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            self.__tail.prev.next = node
            node.prev = self.__tail.prev
            node.next = self.__tail
            self.__tail.prev = node

            return val
        else:
            return -1  

    def put(self, key: int, value: int) -> None:

        # if in the map already, update value and move
        # node to the end of the list
        if key in self.__map:

            # move from the middle to the tail
            node = self.__map[key]
            node.val = (key, value) # update value
            node.prev.next = node.next
            node.next.prev = node.prev

            self.__tail.prev.next = node
            node.prev = self.__tail.prev
            node.next = self.__tail
            self.__tail.prev = node
        
        else:

            # if at max capacity, we evict from the head
            if len(self.__map) == self.__capacity:

                evict_key = self.__head.next.val[0]
                self.__map.pop(evict_key)
                self.__head.next = self.__head.next.next
                self.__head.next.prev = self.__head

            # make new node and append to tail
            node = Node((key, value))

            if len(self.__map) == 0:
                self.__head.next = node
                node.prev = self.__head
                node.next = self.__tail
                self.__tail.prev = node
            else:
                self.__tail.prev.next = node
                node.prev = self.__tail.prev
                node.next = self.__tail
                self.__tail.prev = node

            self.__map[key] = node
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
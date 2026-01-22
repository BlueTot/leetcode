from heapq import nlargest, heappop, heappush

class Node:

    def __init__(self, time, value, next=None):
        self.time = time
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.time},{self.value},{self.next})"

    def __lt__(self, other):
        return self.time > other.time

class Twitter:

    def __init__(self):
        self.__tweets = {}
        self.__follows = {}
        self.__time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # we build a linked list of tweets
        # the latest is at the very end
        # pointers point towards the start
        if userId not in self.__tweets:
            self.__tweets[userId] = Node(self.__time, tweetId)
        else:
            prev = self.__tweets[userId]
            self.__tweets[userId] = Node(self.__time, tweetId)
            self.__tweets[userId].next = prev
        self.__time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        if userId in self.__tweets:
            heappush(heap, self.__tweets[userId])
        for followerId in self.__follows.get(userId, set()):
            if followerId in self.__tweets:
                heappush(heap, self.__tweets[followerId])

        # print(heap)
        res = []
        while (heap and len(res) < 10):
            node = heappop(heap)
            res.append(node.value)
            if node.next is not None:
                heappush(heap, node.next)
    
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.__follows:
            self.__follows[followerId] = set()
        self.__follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.__follows:
            self.__follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
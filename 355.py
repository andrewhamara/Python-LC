class Twitter:
    whoTweetedWhat = []
    whoFollowsWho = []
    def __init__(self):
        self.whoFollowsWho = {}
        self.whoTweetedWhat = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.whoTweetedWhat.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = 0
        feed = []
        for n in reversed(self.whoTweetedWhat):
            if (userId in self.whoFollowsWho and n[0] in self.whoFollowsWho[userId]) or n[0] == userId:
                feed.append(n[1])
                tweets += 1
            if tweets == 10:
                break
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.whoFollowsWho:
            self.whoFollowsWho[followerId].append(followeeId)
        else:
            self.whoFollowsWho[followerId] = [followeeId]

    def unfollow(self, followerId, followeeId: int) -> None:
        if followerId in self.whoFollowsWho and followeeId in self.whoFollowsWho[followerId]:
            self.whoFollowsWho[followerId].remove(followeeId)

#O.E. #3
#Mark J. Rullan

class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"Logging in as {self.username}...")

    def post(self, content):
        print(f"{self.username} posted: {content}")

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self, story_content):
        print(f"{self.username} shared a story: {story_content}")

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self, tweet_content):
        print(f"{self.username} tweeted: {tweet_content}")

instagram_account = InstagramAccount("insta_user", "password123", 5000)
instagram_account.login()
instagram_account.post("Hello, Instagram!")
instagram_account.share_story("A beautiful sunset")

twitter_account = TwitterAccount("twitter_user", "password456", 1000)
twitter_account.login()  
twitter_account.post("Hello, Twitter!")
twitter_account.tweet("Just had coffee!")

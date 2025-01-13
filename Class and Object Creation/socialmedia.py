class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        if not self.posts:
            print(f'User {self.username} has no posts yet.')
        else:
            for index, item in enumerate(self.posts, start=1):
                print(f"User's {self.username} post {index}: {item}")

new_user = SocialMediaProfile('johndoe')
new_user.add_post('Hello, world!')
new_user.add_post('Had a great day at the park!')
new_user.add_post("What's up, Natalie? How are you?")

new_user.display_timeline()
    

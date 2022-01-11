class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


first_user = BlogPost('Mike', 'something text one', 102)
second_user = BlogPost('Jon', 'something text two', 76)

first_user.number_of_likes = 123

print(first_user.number_of_likes)
print(second_user.number_of_likes)

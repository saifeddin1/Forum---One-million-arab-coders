
#--------------------------- Models -------------------------------

import datetime


class Member:
    def __init__(self, name, age):
        self.id = 0
        self.name = name
        self.age = age
        self.posts = []

    def __str__(self):
        return "Name: {}, Age: {}".format(self.name, self.age)


class Post:
    def __init__(self, title, content, member_id=0):
        self.id = 0
        self.title = title
        self.content = content
        self.member_id = member_id
        self.date = datetime.datetime.now()

    def __str__(self):
return f"Title: {self.title}, Content: {self.content}, Date: {self.date}"

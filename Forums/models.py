
#--------------------------- Models -------------------------------

class Member():
    id = 0
    def __init__(self, name, age, id):
        self.id = 0
        self.name = name
        self.age = age

class Post():
    def __init__(self, title, topic):
        self.title = title
        self.topic = topic

    @staticmethod
    def separator():
        print("=" * 40)

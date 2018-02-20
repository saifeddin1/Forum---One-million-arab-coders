
#--------------------------- Models -------------------------------

class Member():
    
    def __init__(self, name, age, id):
        self.id = 0
        self.name = name
        self.age = age

class Post():
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @staticmethod
    def separator():
        print("=" * 40)

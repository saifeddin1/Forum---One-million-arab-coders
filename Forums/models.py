class Member():
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Post():
	def __init__(self, title, topic):
		self.title = title
		self.topic = topic 

#~~~~~~~~~~~~~Stores~~~~~~~~~~~#
class MemberStore():
	members = []
	
	def add(self, member):
		MemberStore.members.append(member)
	
	def getall(self):
		for member in MemberStore.members:
			return self.members
		

	
class Post_store():
	posts = []
	
	def add(self, post):
		Post_store.posts.append(post)
		
	def get_all():
		for post in Post_store.posts:
			return self.posts
		

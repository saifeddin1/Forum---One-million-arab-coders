#~~~~~~~~~~~~~Stores~~~~~~~~~~~#
class MemberStore():
	members = []
	
	def add(self, member):
		MemberStore.members.append(member)
	
	def get_all(self):
		for member in MemberStore.members:
			return self.members
		

	
class PostStore():
	posts = []
	
	def add(self, post):
		Post_store.posts.append(post)
		
	def get_all():
		for post in Post_store.posts:
			return self.posts
		


#~~~~~~~~~~~~~Stores~~~~~~~~~~~#
class MemberStore():
   
    members = []
    last_id = 1
    
    def add(self, member):
        member.id = MemberStore.last_id

        MemberStore.members.append(member)
        
        MemberStore.last_id += 1
    
    def get_by_id(self, id):
        all_members = self.get_all()
        for member in all_members:
            result = member
        return result


    def get_all(self):
        for member in MemberStore.members:
            return self.members
    
    def entity_exists(self, member):
        result = True
        if member.id in MemberStore:
            return result
        else:
            return False
        
        
        

    
class PostStore():
    posts = []
    
    def add(self, post):
        PostStore.posts.append(post)
        
    def get_all(self):
        for post in PostStore.posts:
            return self.posts

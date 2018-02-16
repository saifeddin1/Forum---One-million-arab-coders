
#---------------------------------- Main -----------------------------------

#Starting..

      #Importing classes from the existing files models and stores
import models
from stores import MemberStore, PostStore

#Creating members
member1 = models.Member("Mohamed", 15)
member2 = models.Member("Karim", 25)

member_store = MemberStore()
my_posts = PostStore()

#Decoration
post1 = models.Post("*Python", "Python Programming\n" *5)
post2 = models.Post("*OOP", "Object Oriented Programming\n" *5)
post3 = models.Post("*Nothing", "Nothing Here!\n" * 5)
#Starting
print("*****" * 15)
print("                       One Million Arab Coders Forum (sample)")
print("*****" * 15)
print("-" * 20, "\n", "Members")
print("-" * 20)
#Show member and their informations
print(member1.name + "," + str(member1.age))
print(member2.name + "," + str(member2.age))
print("-" * 20, "\n", "Posts")
print("-" * 20)

#Posts Area
print(post1.title, "\n",post1.topic)
print(post2.title, "\n", post2.topic)
print(post3.title, "\n", post3.topic)
models.Post.separator()

member_store.add(member1)
member_store.add(member2)
print(member_store.get_all())
my_posts.add(post1)
my_posts.add(post2)
my_posts.add(post3)
print(my_posts.get_all())
print(my_posts.get_all)


from models import Member
from models import Post

member1 = Member("Mohamed", 15)
member2 = Member("Karim", 25)

post1 = Post("*Python", "Python Programming\n" *5)
post2 = Post("*OOP", "Object Oriented Programming\n" *5)
post3 = Post("*Nothing", "Nothing Here!\n" * 5)
#Starting
print("******" * 15)
print("                       One Million Arab Coders Forum (sample)")
print("******" * 15)
print("-" * 20, "\n", "Members")
print("-" * 20)
print(member1.name + "," + str(member1.age))
print(member2.name + "," + str(member2.age))

print("-" * 20, "\n", "Posts")
print("-" * 20)

print(post1.title, "\n",post1.topic)
print(post2.title, "\n", post2.topic)
print(post3.title, "\n", post3.topic)
from blog import db
from blog.models import User, Post, Comment

db.drop_all()
db.create_all()

user1 = User(
    username="testperson",
    password="123",
)

user2 = User(username="user1@test.ac.uk", password="passuser1")



post1 = Post(
    title="My First Post",
    author="Pitnaree",
    slug="fist_post",
    content="Hello! This is my first blog post! My name is Pitnaree. I'm currently studying Msc Computing at Cardiff University. Before I came to UK, I used to live in Thailand. I worked as a 3d artist in some game companies in Thailand. It was very interesting job but I also very intested in Technlogy so I decided to come to UK to learn programming. My posts will be something that I interested in. I hope my readers will enjoy this! Thank you! see you next post!",
    user_id=1
)
post2 = Post(
    title="gaming",
    author="Pitnaree",
    slug="second_post",
    content="Hello! This is my second blog post! Recently, I've been very busy with the assessment. I wish I have more time to understand all the coursework. I heard some pleasant news from the company that create the game that I've been playing for more than ten years. It's the sims. The new game pack is coming and it focus on wedding theme. It seems to be a decent game pack which there will be a livestream from devs coming on this Friday! Looking forward!",
    user_id=1
)

post3 = Post(
    title="Good news",
    author="Pitnaree",
    slug="third_post",
    content="Hello! Bitcoin price is recovered.",
    user_id=1
)

comment1 = Comment(text='Hello', user_id ='testperson' , user=user1, post=post1)

db.session.add(user1)
db.session.add(user2)


db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.add(comment1)

db.session.commit()
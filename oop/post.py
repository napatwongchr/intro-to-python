post_list = []

class Post():
  def __init__(self, title, content, user):
    self.title = title
    self.content = content
    self.user = user

  def get_title(self):
    return self.title
  
  def get_content(self):
    return self.content
  
  def get_author(self):
    return self.user

  def __str__(self):
    return f"<<Post object: title={self.title}>>"

class Author():
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def create_post(self, post):
    post_list.append(post)

  def update_post(self, new_title, new_content):
    None

  def delete_post(self, post_id):
    None


john = Author(1, "John")

abe = Author(2, "Abe")

post = Post("try oop", "oop content", john)

john.create_post(post)

other_post = Post("how to be a millionaire", "you must win a lottery prize", abe)

abe.create_post(other_post)

print(post_list)

print(str(post_list[0]))

print(str(post_list[1]))

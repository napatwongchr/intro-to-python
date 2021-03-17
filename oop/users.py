class User:
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def increase_score(self):
    self.score += 1

  def get_score(self):
    return self.score

  def __str__(self):
      return f"<<User object: name={self.name} score={self.score}>>"

class Customer(User):
  def __init__(self, name, score):
    super().__init__(name, score)


user_1 = User("John", 0)
user_2 = User("John", 0)

user_1.increase_score()
user_1.increase_score()

user_2.increase_score()

user_1_score = user_1.get_score()
user_2_score = user_2.get_score()

print(f"user_1_score: {user_1_score}")
print(f"user_2_score: {user_2_score}")


print(f"This is user_1 detail: {str(user_1)}")

customer_1 = Customer("Abe", 10)
print(f"This is customer_1 detail: {str(customer_1)}")

from datetime import datetime, timedelta

class Restaurant:
  def __init__(self, name, total_capacity, open_at, closed_at):
    self.name = name
    self.total_capacity = total_capacity
    self.current_capacity = 0
    self.open_at = open_at
    self.closed_at = closed_at

  def get_total_capacity(self):
    return self.total_capacity
  
  def get_open_time(self):
    return self.open_at

  def get_close_time(self):
    return self.closed_at

  def reserve_seat(self, customer):
    if self.current_capacity < self.total_capacity:
      self.current_capacity += 1
      print(f"Reserve success success, current capacity is : {self.current_capacity}")
    else:
      print(f"Reserve failed capacity full, current capacity is : {self.current_capacity}")

  def get_reserved_restaurant(self):
    None
  
  def __str__(self):
    return f"<<Restaurant object: {self.name} capacity is {self.current_capacity}>>"
    
class Customer:
  def __init__(self, name, age, birthdate):
    self.name = name
    self.age = age
    self.birthdate = birthdate
  
  def get_customer_details(self):
    None

  def __str__(self):
    return f"<<Customer object: {self.name} >>"


# Actions
today = datetime.now() 
tmr = datetime.now() + timedelta(days=1)

mk = Restaurant(name='MK', total_capacity=2, open_at=today, closed_at=tmr)
momo = Restaurant(name='MOMO', total_capacity=10, open_at=today, closed_at=tmr)

knot = Customer(name="Knot", age=26, birthdate=tmr)
jan = Customer(name="Jan", age=26, birthdate=tmr)

mk.reserve_seat(knot)

print(mk)

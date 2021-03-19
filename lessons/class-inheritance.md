# Class Inheritance

Class inheritance มีประโยชน์มากในการ reuse code

Inheritance สามารถจัดโครงสร้าง code เราให้อยู่ในรูปแบบ hierachy ได้

ลองมาดูตัวอย่างกัน

```python
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
```

<br><hr><br>

## isinstance

เราสามารถเช็ค instance ที่เราสร้างมาได้ว่าเป็น instance ของ class นั้นจริง ๆ หรือเปล่า ยกตัวอย่างเช่น

```python
print(isinstance(customer_1, User)) # True
```

<br><hr><br>

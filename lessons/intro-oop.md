# Object Oriented Programming (OOP)

การเขียนโปรแกรมนั้นมีหลากหลายรูปแบบ รูปแบบที่เราเห็นบ่อย และดูคุ้นเคยมากที่สุดคือ **Procedural Programming**

Procedural Programming เป็นรูปแบบการเขียนโปรแกรมที่เราแบ่งการทำงานของโปรแกรมออกไปเป็น Function ย่อย ๆ หลายๆ ตัว และเราก็จะมีข้อมูลในโปรแกรมของเราถูกเก็บไว้ใน Variables หลาย ๆ ตัว แล้วก็เรียกใช้ Function เพื่อที่จะทำอะไรสักอย่างเกี่ยวกับ Variables เหล่านั้น

ยกตัวอย่างเช่น

```python
user_1_name = "John";
user_2_name = "Micky";

user_1_score = 0;
user_2_score = 0;

def increase_score(score):
  return score + 1

user_1_score = increase_score(user_1_score);
user_2_score = increase_score(user_2_score);
```

เมื่อเวลาผ่านไป โปรแกรมของเราเริ่มใหญ่ขึ้น Functions และ Variables ก็จะมีเยอะมากขึ้น ซึ่งอาจจะมีการเขียนซ้ำกันไปมา เรียกใช้กันไปกันมาอย่างไม่เป็นระบบระเบียบ ในสุด Code เราจะก็จะดูยุ่งยาก หรือเรียกว่า **"Spaghetti Code"**

มันก็มีแนวคิดขึ้นมาว่าถ้าเราจัดรูปแบบการเขียนโปรแกรมเราใหม่ ถ้าเรารวบ Functions และ Variables ที่เกี่ยวข้องกันเข้าไว้ด้วยกันน่าจะทำให้ Code โปรแกรมเป็นระบบระเบียบ และดูแลรักษาง่ายมากยิ่งขึ้น รูปแบบนี้เรียกว่า **Object Oriented Programming (OOP)**

OOP คือ รูปแบบการเขียนโปรแกรมอย่างหนึ่ง ที่ทำการจัดกลุ่ม Variables และ Functions ที่เกี่ยวข้องกันให้มาอยู่ด้วยกันเป็นก้อนเดียวกัน ก้อน นี้เราจะเรียกว่า **Object**

🌟 ใน Object เราจะเรียก **ariables ว่า Properties** และ **Functions ว่า Methods**

🌟 **Object สามารถสร้างด้วย Class** เราจะเรียก process นี้ว่า **Instantiation** และ Object ที่สร้างมาเราสามารถเรียกมันได้ว่าเป็น **Instance** ตัวนึง

<br><hr><br>

## Creating Object (Instantiation)

เราลองมาดูตัวอย่างกัน

```python
class User:
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def increase_score(self):
    self.score += 1

  def get_score(self):
    return self.score
```

## self

เราจะเห็นได้ว่าใน class ของเรามีคำว่า **self** ซึ่ง self คือ variable ตัวนึงใน class ที่ผูกกับ variables ของ instance นั้น ๆ

## `__init__()`

Classes จะมี method แปลก ๆ คือ `__init__()` เป็น method ที่จะถูกเรียกใช้งานเมื่อเราสร้าง instance **init**() และสามารถรับ arguments ได้ จากตัวอย่างข้างบนเรารับ name และ score เข้ามา

เมื่อมี Class แล้วจากนั้นเรามาสร้าง Object User กัน

```python
user_1 = User("John", 0)
user_2 = User("John", 0)

user_1.increase_score()
user_1.increase_score()

user_2.increase_score()

user_1_score = user_1.get_score()
user_2_score = user_2.get_score()

print(f"user_1_score: {user_1_score}")
print(f"user_2_score: {user_2_score}")
```

🌟 การรวบ Properties และ Methods เข้าไว้ด้วยกันเป็น Object เราจะเรียกตรงนี้ว่า **"Encapsulation"**

🌟 **User เป็น data type** ตัวนึง จากตัวอย่างข้างบน user_1 มี type เป็น User

## `__str__()`

**str**() เป็น method ตัวนึงที่อยู่ใน class ที่มีหน้าที่ช่วยเราในการ **debug**

ลองมาดูตัวอย่างกัน

```python
class User:

  # Skipped code

  def __str__(self):
      return f"<<User object: name={self.name} score={self.score}>>"

user_1 = User("John", 0)

print(f"This is user_1 detail: {str(user_1)}")
```

<br><hr><br>

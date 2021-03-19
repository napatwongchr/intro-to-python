# List Comprehension

เราลองมาดูโจทย์กันสักหน่อย

โจทย์คือ ถ้าเรามี list ของ numbers **เราอยากจะสร้าง list ใหม่ให้ number แต่ละตัวใน list เพิ่มขึ้น 2 เท่า** เราทำยังไงได้บ้าง ?

การที่จัดการของ**แต่ละ**ชิ้น คำว่าแต่ละ เราน่าจะต้องมองเรื่องของ loop เราจะเอา number list มา loop แล้ว นำตัวเลขแต่ละตัวไป x2 จากนั้นค่อยนำไปใส่ใน list ใหม่ ตามที่โจทย์ต้องการ

```python
numbers = [1, 2, 3, 4, 5]
result_numbers = []

for number in numbers:
  new_number = number * 2
  result_numbers.append(new_number)

print(result_numbers)
```

ลองมาดูอีกสักโจทย์

ถ้าเรามี list ของชื่อ employee เราอยากจะติด Tag รหัสหน่วยงานเข้าไปในชื่อพนักงานว่า "ADMIN" ออกมาเป็น list ใหม่

```python
employee_names = ["John", "G", "Abe"]
result_employee_names = []

for employee_name in employee_names:
  employee_name_with_tag = f"ADMIN-{employee_name}"
  result_employee_names.append(employee_name_with_tag)

print(result_employee_names)
```

🌟 ใน Python มีรูปแบบการเขียนโจทย์ข้างบนให้ง่ายมากยิ่งขึ้น เราเรียกว่า **"List Comprehension"**

สำหรับโจทย์แรกที่เรา loop แบบปกติเราสามารถเขียนแบบนี้ได้

```python
numbers = [1, 2, 3, 4, 5]

result_numbers = [number  * 2 for number in numbers]

print(result_numbers)
```

สำหรับโจทย์ต่อมา

```python
employee_names = ["John", "G", "Abe"]

result_employee_names = [f"ADMIN-{employee_name}" for employee_name in employee_names]

print(result_employee_names)
```

ลองมาดูตัวอย่างที่น่าสนในอีกซักตัวอย่าง ถ้าเรามี employee list แบบนี้

```python
employees = [
    { "name": 'Bradley', "age": 20, "points": 3  },
    { "name": 'Chloe', "age": 40, "points": 6 },
    { "name": 'Robert', "age": 34, "points": 8 },
    { "name": 'Wes', "age": 25, "points": 10},
    { "name": 'Zach', "age": 67, "points": 7}
]
```

โจทย์คือ ถ้าเราอยากจะได้ list ของ employee ที่มีข้อมูล age > 30 เราสามารถทำแบบนี้ได้

```python
new_employees = [employee for employee in employees if employee["age"] > 30]
print(new_employees)
```

โจทย์ต่อมา ถ้าเราอยากได้ list ของ employee ที่มีข้อมูล status = "Passed" ในแต่ละ employee เราสามารถทำแบบนี้ได้

```python
new_employees = [dict(employee, status="Passed") for employee in employees if employee["age"] > 30]
print(new_employees)
```

ต่อไปถ้าเราอยากได้ผลรวมของอายุ employees

```python
new_employees = sum([employee["age"] for employee in employees])
print(new_employees)
```

<br><hr><br>

## Conditionals List Comprehension

มาลองดูโจทย์ใหม่กัน ถ้าเราบอกว่าเราอยากจะกรองชื่อจาก employee_names list ที่ความยาวมากกว่า 3 ตัวอักษร ให้ออกมาเป็น list ใหม่ เราสามารถทำยังไงได้บ้าง

```python
employee_names = ["John", "G", "Abe"]

result_employee_names = [employee_name for employee_name in employee_names if len(employee_name) > 3]

print(result_employee_names)
```

<br><hr><br>

<div>
  <span style="font-size: 32px; text-align:center">
  🌟 หลักการเขียน List Comprehension

**[ (Return Result) (Loop) (Condition) ]**
</span>

</div>

<br><hr><br>

## Exercises 🏅

กำหนดให้

```python
users = [
      { "first_name": 'Bradley', "last_name": 'Bouley', "role": 'Full Stack Resident', "salary", 200000 },
      { "first_name": 'Chloe', "last_name": 'Alnaji', "role": 'Full Stack Resident', "salary", 45000 },
      { "first_name": 'Jonathan', "last_name": 'Baughn', "role": 'Enterprise Instructor', "salary", 500000 },
      { "first_name": 'Michael', "last_name": 'Herman', "role": 'Lead Instructor', "salary", 100000 },
      { "first_name": 'Robert', "last_name": 'Hajek', "role": 'Full Stack Resident', "salary", 150000 },
      { "first_name": 'Wes', "last_name": 'Reid', "role": 'Instructor', "salary", 30400},
      { "first_name": 'Zach', "last_name": 'Klabunde', "role": 'Instructor', "salary", 350000}
    ]
```

A) ให้สร้าง List ใหม่ที่ user มี role เป็น "Instructor" เท่านั้น

B) ให้สร้าง List ใหม่ที่ user มีข้อมูล grade (สมมุติให้ grade เป็น "A")

C) ให้สร้าง List ใหม่ที่ first_name ของแต่ละ user ติด Tag "A001" เข้าไปหน้าชื่อ

D) ผลรวมของ Salary ในแต่ละ user ทั้งหมดเท่าไหร่

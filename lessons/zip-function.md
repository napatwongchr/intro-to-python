# Zip Function

Zip function เป็น function ที่ return zip object ที่สามารถรวบ values แต่ละชิ้นของทั้งสอง list เข้าด้วยกันได้

```python
employees = ["John", "G", "Abe"]
scores = [40, 20, 50]

zip(employees, scores)
```

เราสามารถที่จะเปลี่ยน zip object เป็น list ได้

```python
list(zip(employees, scores))
```

เราสามารถ loop zip object ได้

```python
for employee, score in zip(employees, scores):
  print (f"Employee: {employee}, Score: {score}")
```

🌟 เราสามารถ zip แล้วนำไปสร้างเป็น dict ได้

```python
employee_details = dict(zip(employees, scores))
print(employee_details)
```

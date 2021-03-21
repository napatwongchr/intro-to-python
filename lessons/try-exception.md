# Try And Exception

**โครงสร้าง try exception**

```python
try:
    <code to try>
except ExceptionClass:
    <code to run if an exception happens>
```

**ตัวอย่าง**

```python
try:
    x = int(input("Please enter a number: "))
except ValueError:
    print("Oops!  That was no valid number.  Try again...")
```

เราจําเป็นต้องรู้ Exception Class ว่า Error Exception ที่เกิดขึ้นคืออะไร เช่น ValueError, KeyError, TypeError, Etc.

ข้อมูลเพิ่มเติมเกี่ยวกับ [Python Exception List](https://docs.python.org/3/library/exceptions.html)

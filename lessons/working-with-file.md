# Working With File

ปกติเราจะอ่านไฟล์ด้วย built-in function ที่ชื่อว่า `open` แต่เราจะใช้กับ `with` ซึ่งเป็น **context manager**

Context manager จะเป็นตัวที่คอยจัดการการเปิดปิดไฟล์ให้เราอย่างมีประสิทธิภาพ ปกติเวลาเรา จะอ่านไฟลเ์ราจะตอ้งopen()จากนั้นเมื่ออ่านเสร็จให้เราclose()ดว้ยเสมอๆแต่ถ้าใช้context manager มันจะ close() ให้เราเอง

ให้ download ตัวอย่างไฟล์ text [ที่นี่](../working-with-file/hello.txt)

เราสามารถที่จะอ่านข้อมูลจากไฟล์ได้แบบนี้

```python
from pathlib import Path

def read_text_file():
  filepath =  Path().absolute() / "working-with-file" / "hello.txt"

  with open(filepath) as my_file:
      contents = my_file.read()
      print(contents)

read_text_file()
```

เรามาลองดูการอ่านไฟล์ json กันบ้าง

ให้ download ตัวอย่างไฟล์ได้ [ที่นี่](../working-with-file/users.json)

```python
from pathlib import Path
import json

def read_json_file():
  filepath =  Path().absolute() / "working-with-file" / "users.json"

  with open(filepath) as users_file:
      users_raw_data = users_file.read()
      users_json = json.loads(users_raw_data)
      print(users_json)

read_json_file()
```

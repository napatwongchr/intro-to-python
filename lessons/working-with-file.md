# Working With File

เราสามารถที่จะอ่านข้อมูลจากไฟล์ได้แบบนี้

ให้ download ตัวอย่างไฟล์ได้ [ที่นี่](../../intro-to-python/working-with-file/hello.txt)

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

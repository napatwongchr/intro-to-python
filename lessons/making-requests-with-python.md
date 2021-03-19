# Making Request With Python

เราจะใช้ requests library ในการ connect กับ apis

```python
import requests

endpoint = "https://dog.ceo/api/breeds/image/random"

response = requests.get(endpoint)

response_json = response.json()

print(response_json)
```

[ข้อมูลเพิ่มเติมเกี่ยวกับ requests library](https://2.python-requests.org/en/master/user/quickstart/)

<br><hr><br>

## Exercises 🏅

ให้ลองเลือก API อะไรก็ได้จาก [Public APIs Repository](https://github.com/public-apis/public-apis) ที่มี Auth เป็น No และ Cors เป็น No แล้วลอง make get request ไปขอข้อมูล

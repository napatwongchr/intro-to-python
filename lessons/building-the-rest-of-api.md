# Building the rest of APIs

มาลองสร้าง API ตัวอื่น ๆ กัน จาก API Document ของเราตามนี้

| Method | Path       | Description       | Request Body                                         |
| ------ | ---------- | ----------------- | ---------------------------------------------------- |
| GET    | /posts     | Get all posts     | None                                                 |
| GET    | /posts/:id | Get post by id    | None                                                 |
| POST   | /posts/    | Create post       | { "title": "post title", "content": "post content" } |
| PUT    | /posts/:id | Update post by id | { "title": "post title", "content": "post content" } |
| DELETE | /posts/:id | Delete post by id | None                                                 |

<br><hr><br>

## Get Post By Id

ยังเหลือ APIs ขาอื่นๆ ที่เรายังไม่ได้ทำ เรามาลองดูการดึงข้อมูล post ด้วย id (GET /posts/:id) เริ่มแรก ให้เราสร้าง view function ก่อน ที่ไฟล์ `posts/views.py` เหมือนเดิม ชื่อว่า single_post_detail และ return JsonResponse ออกไปเป็น dictionary

```python
def single_post_detail(request):
  response = JsonResponse({ "data": {} })
  return response
```

ต่อไปเราต้อง link `single_post_detial` view เข้ากับ endpoint path ที่ไฟล์ `posts/urls.py` แบบนี้

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<str:post_id>', views.single_post_detail, name='single_post_detail'),
]
```

ซึ่งจะแตกต่างจากตัวก่อน เพราะว่าเป็น path ที่มี parameter วิธีการสร้าง path ที่มี parameter ให้เราใช้ **<>** ข้างใน path string ที่เราส่งเข้าไปใน path function

และเราสามารถเรียกใช้ parameter post_id จาก parameter ตัวที่ 2 ของ view function จากนั้นเราจะทำการ filter posts ด้วย post_id ที่ส่งเข้ามาแล้ว return ออกไป

```python
def single_post_detail(request, post_id):
  response = JsonResponse({ "data": {} })

  for post in posts["data”]:
    if post["id"] == post_id:
      response = JsonResponse({ "data": post })
      return response

  response.status_code = 404
  return response

```

<br><hr><br>

## Create Post

เราจะมาลอง create post กันบ้าง

การ create เราจะใช้ Http method post และ path เป็น /posts/

ให้สังเกต path มันเหมือนกันกับ get post list ที่เราสร้างไว้ เราจะใช้ path เดียวกัน

แต่เราจะไปแยก http method ข้างใน post_list function request parameter เป็น dictionary ที่มี key method ที่สามารถบอกได้ว่า request ที่เข้ามาเป็นอะไร

```python
def post_list(request):
  if (request.method == "GET"):
    response = JsonResponse(data=posts)
    response.status_code = 200
    return response

  if (request.method == "POST"):
    response = JsonResponse(data={})
    response.status_code = 201
    return response
```

เมื่อเรา refactor code เรียบร้อยให้เราไปลอง test api ดูที่ postman ว่า API get post list ของเรายังทำงานได้ไหม

จากนั้นไปลอง test api create post ที่เราสร้างขึ้นมาเราจะได้ error ขึ้นมาว่า

`Forbidden (403) CSRF verification failed`

เนื่องจาก django มีการป้องกันการทำ Cross-Site Request Forgery (CSRF)

CSRF คือ การที่คนอื่นขโมย creadential ของเราไปได้ แล้วใช้ตัวตนของเรานั้น ไปทำ action ต่าง ๆ บน web app ที่เราใช้งานได้

ซึ่งการ GET ได้รับการยกเว้นเราเลยไม่เจอ CSRF error

แต่ถ้าเป็น **POST PUT DELETE** จะได้รับ error ในที่นี้เราจะทำการ bypass CSRF validation ให้ผ่านไปก่อน

ด้วยการ import `csrf_exempt` มาจาก `django.views.decorators.csrf` แล้วให้ใส่ @csrf_exempt ไว้ข้างบน post_list function ของเรา

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post_list(request):
  if (request.method == "GET"):
    response = JsonResponse(data=posts)
    response.status_code = 200
    return response

  if (request.method == "POST"):
    response = JsonResponse(data={})
    response.status_code = 201
    return response
```

จากนั้นเราจะมาลองเขียน logic การสร้าง post กันครับ

```python
if (request.method == "POST"):
    data = json.loads(request.body)
    posts["data"].append({ "id": "2", "title": data["title"], "content": data["content"] })
    response = JsonResponse(data={ "message": "created post successfully." })
    response.status_code = 201
    return response
```

<br><hr><br>

## Exercise 🏅

1. ลองเขียน API Update Post

2. ลองเขียน API Delete Post

<br><hr><br>

# Object Relational Mapper (ORM)

เราสามารถเขียน Raw Queries เพื่อที่จะทำ DB Operations ต่างได้ผ่าน Cursor แต่มันจะดีกว่าไหมถ้าเราสามารถที่จะ**ใช้ Concept ของ Class ในการทำ DB Operations** เพื่อที่ทำให้เรา Focus ในการเขียน App ได้มากขึ้น โดยไม่ต้องกังวลกับ SQL Statements สิ่งนี้เราจะเรียกว่า **"Object Relational Mapper (ORM)"**

<br><hr><br>

## First ORM !

```python
@csrf_exempt
def post_list(request):

  if (request.method == "GET"):
    queried_posts = Post.objects.all()

    data = list(queried_posts.values())

    response_data = {}
    response_data['data'] = data

    response = HttpResponse(
      json.dumps(response_data),
      content_type='application/json'
    )

    response.status_code = 200
    return response
```

<br><hr><br>

## Insert Data Into DB With ORM

เราจะสร้าง Post instance ที่ import มาจาก `from .models import Post` จากนั้นเราจะส่ง arguments title และ content เข้าไป แล้วเรา save ข้อมูลลง db ด้วย `post.save()`

```python
if (request.method == "POST"):
    data = json.loads(request.body)

    post = Post(
      title=data["title"],
      content=data["content"]
    )

    post.save()

    response = JsonResponse(data={ "message": "created post successfully." })
    response.status_code = 201
    return response
```

<br><hr><br>

## Get Post By Id With ORM

```python
@csrf_exempt
def single_post_detail(request, post_id):
  if request.method == "GET":
    try:
      queried_post = Post.objects.filter(id=post_id)
      data = queried_post.values()[0]
    except DataError:
      response_data = {}
      response_data['message'] = "Invalid request"
      response_data['data'] = []

      response = HttpResponse(
        json.dumps(response_data),
        content_type='application/json'
      )
      response.status_code = 400
      return response


    response_data = {}
    response_data['data'] = data

    response = HttpResponse(
      json.dumps(response_data),
      content_type='application/json'
    )

    response.status_code = 200

    return response
```

<br><hr><br>

## Update Post With ORM

หลักการของการ Update เราต้องดึง Post ตัวที่เราจะ Update ขึ้นมาก่อนจากนั้นทำการ reassign ค่าใหม่เข้าไปใน fields ข้อมูล

```python
if request.method == "PUT":
    request_data = json.loads(request.body)

    try:
      queried_post = Post.objects.filter(id=post_id)[0]
      queried_post.title = request_data["title"]
      queried_post.content = request_data["content"]
      queried_post.save()

    except DataError:
      response_data = {}
      response_data['message'] = "Invalid request"

      response = HttpResponse(
        json.dumps(response_data),
        content_type='application/json'
      )
      response.status_code = 400
      return response

    response = JsonResponse(data={ "message": "updated post successfully." })
    response.status_code = 200
    return response
```

<br><hr><br>

## Delete Post With ORM

ให้ filter หาข้อมูลที่จะลบออกมาด้วย post_id จากนั้นเรียกใช้ delete function

```python
if request.method == "DELETE":
    try:
      queried_post = Post.objects.filter(id=post_id)[0]
      queried_post.delete()
    except DataError:
      response_data = {}
      response_data['message'] = "Invalid request"

      response = HttpResponse(
        json.dumps(response_data),
        content_type='application/json'
      )
      response.status_code = 400
      return response

    response = JsonResponse(data={ "message": "deleted post successfully."})
    response.status = 200
    return response
```

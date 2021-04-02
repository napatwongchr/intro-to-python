# Making Raw Query On Django

การเขียน query statement เพื่อที่จะทำ operation เกี่ยวกับข้อมูลใน database เราจะทำผ่านสิ่งที่เรียกว่า "cursor" ให้คิดว่า cursor เป็นคนกลางที่จะรับ query statement เราไปเพื่อไปค้นข้อมูล และทำ operation กับข้อมูลเราใน database

<br><hr><br>

## First Raw Query

เราจะเขียน query เพื่อดึงข้อมูลจาก database จริง ๆ ให้เริ่มจาก api get all posts

```python
@csrf_exempt
def post_list(request):

  if (request.method == "GET"):
    with connections['default'].cursor() as cursor:
      cursor.execute("SELECT * FROM posts_post")

      columns = [col[0] for col in cursor.description]

      data = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
      ]


    response_data = {}
    response_data['data'] = data

    response = HttpResponse(
      json.dumps(response_data),
      content_type='application/json'
    )

    response.status_code = 200
    return response
```

จาก code ข้างต้น

- เราทำการต่อ connection เข้าไป default databas ซึ่งใน `settings.py` เราะได้กำหนดไว้ว่า default db ของเราคือ postgres
- จากนั้นเราเรียกใช้ cursor การที่เราจะส่ง query statement เข้าไปหา database ได้เราจะใช้สิ่งที่เรียกว่า cursor ในการทำ
- เราจะส่ง query statement เพื่อดึงข้อมูล posts แบบนี้ `cursor.execute("SELECT * FROM posts_post")`
- เมื่อ cursor ได้ข้อมูลกลับมาเราจะต้องปั้นหน้าตาของข้อมูลออกไปเป็น response อันดับแรกให้เรา access column ใน `cursor.description` แล้วปั้นออกมาเป็น list
- ต่อไปเราจะทำการ fetch row ข้อมูลด้วย `cursor.fetchall()`
- จากนั้นเราจะ zip row เข้ากับ column ที่เราเก็บไว้ใน list แล้วเปลี่ยนเป็น dictionary เพื่อ return ข้อมูลออกไปเป็น response

<br><hr><br>

## Insert Data Into Database

เราจะลอง insert ข้อมูลกันบ้าง

```python
if (request.method == "POST"):
    data = json.loads(request.body)
    with connections['default'].cursor() as cursor:
      cursor.execute('INSERT INTO posts_post (title, content) VALUES (%s, %s)', [data["title"], data["content"]])
    response = JsonResponse(data={ "message": "created post successfully." })
    response.status_code = 201
    return response
```

- ใช้ cursor ในการส่ง query statement เข้าไปทำ db operation เหมือนเดิม
- การที่เราจะส่งข้อมูลจากข้างนอกเข้าไปใน query statement ได้ ให้เราใช้กระบวนการที่เรียกว่า **"Parameterize Query"** แบบนี้ `cursor.execute('INSERT INTO posts_post (title, content) VALUES (%s, %s)', [data["title"], data["content"]])`
- 🌟 🌟 **Parameterize query เป็นสิ่งที่ช่วยเราป้องกัน "SQL Injection" ตรงนี้สำคัญมาก เราไม่ควรนำข้อมูลจาก request ไปฝังลง query statement ตรง ๆ** 🌟 🌟

<br><hr><br>

## Get Post By Id

```python
@csrf_exempt
def single_post_detail(request, post_id):
  if request.method == "GET":
    with connections['default'].cursor() as cursor:
      cursor.execute("SELECT * FROM posts_post WHERE id = %s", [post_id])

      columns = [col[0] for col in cursor.description]

      data = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
      ]

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

## Error Catching

ถ้าเราใส่ Post id ที่ไม่มีใน Database เข้ามาจะเกิด DataError เราต้องดักไว้ด้วย

```python
@csrf_exempt
def single_post_detail(request, post_id):
  if request.method == "GET":
    try:
      with connections['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM posts_post WHERE id = %s", [post_id])

        columns = [col[0] for col in cursor.description]

        data = [
          dict(zip(columns, row))
          for row in cursor.fetchall()
        ]

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

## Update Posts

```python
if request.method == "PUT":
    request_data = json.loads(request.body)

    with connections['default'].cursor() as cursor:
      cursor.execute(
        "UPDATE posts_post SET title=%s, content=%s WHERE id=%s;",
        [request_data["title"], request_data["content"], post_id]
      )

    response = JsonResponse(data={ "message": "updated post successfully." })
    response.status_code = 200
    return response
```

<br><hr><br>

## Delete Post

```python
if request.method == "DELETE":
    with connections['default'].cursor() as cursor:
      cursor.execute(
        "DELETE FROM posts_post WHERE id=%s",
        [post_id]
      )
    response = JsonResponse(data={ "message": "deleted post successfully."})
    response.status = 200
    return response
```

<br><hr><br>

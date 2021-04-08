# Learn django-rest-framework

django-rest-framework เป็นเครื่องมือที่จะช่วยให้เราสร้าง API ได้ง่ายมากยิ่งขึ้นมาก ๆ [สนใจอ่านข้อมูลเพิ่มเติมเกี่ยวกับตัว framework กดที่นี่เลย](https://www.django-rest-framework.org/)

เราจะใช้ django-rest-framework ช่วยเราให้ทำงานง่ายขึ้นใน 2 ส่วนใหญ่ ๆ ของ API ที่เราสร้าง

**1. Serialization ข้อมูล**

เราจะสังเกตเห็นว่า พอเรา query ข้อมูลขึ้นมาจาก Database แล้วเนี่ย เราจะต้องเหมือนกับว่าปั้นข้อมูลให้อยู่ในรูปแบบของ dictionary แล้วทำการเปลี่ยน dictionary ให้กลายเป็น json string เพื่อที่จะส่งข้อมูลกลับไปให้ client ซึ่งมันจะเป็นการเหนื่อยเอามาก ๆ ถ้าเราเขียนตรงนี้ซ้ำไปมาเรื่อย ๆ

**2. API Authentication**

เวลาเราสร้าง API ขึ้นมาเราไม่ได้อยากให้ทุกคนสามารถ Access APIs เราได้อย่างแน่นอน เราจะใช้ django-rest-framework ในการสร้างระบบ Authentication ขึ้นมา

## Setup django-rest-framework

Install django-rest-framework ก่อนด้วยคำสั่ง `pip install djangorestframework`

ใส่ `rest_framework` ลงไปใน INSTALLED_APPS

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'snippets.apps.SnippetsConfig',
]
```

<br><hr><br>

## Serialization

ต่อไปเราจะใช้ django-rest-framework ในการ serialization ข้อมูลที่เรา query ออกมาจาก database

_Serialization เป็นกระบวนการในการเปลี่ยน data structure หรือ object state ให้ไปอยู่ใน format ที่สามารถเก็บลง Database, Memory หรือ File จุดประสงค์หลักคือ เป็นการบันทึกข้อมูล หรือ state นั้น ๆ เอาไว้ เพื่อใช้ในการส่งผ่านข้อมูลไปยังอีกระบบ หรือบันทึกลง database_

สร้างไฟล์ `blogs/serializers.py` แล้วสร้าง PostSerializer, CommentSerializer class ขึ้นมา

```python
from rest_framework import serializers
from .model import Post, Comment

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ['id', 'title', 'content']

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['id', 'comment', 'created_on', 'updated_on']
```

เมื่อเราสร้าง Serializer เสร็จแล้ว เพื่อให้เห็นภาพเรามาลองเล่น Serializer กันซักหน่อยว่ามันนำไปใช้งานเบื้องต้นยังไง เราจะทำการ Refactor API สำหรับ Questions ในการ list comments ทั้งหมด ที่ `blogs/views.py`

```python
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer
from .models import Post, Comment

@api_view(['GET'])
def comment_list(request, post_id):
  if request.method == "GET":
    comments = Comment.objects.filter(post_id=post_id)
    serializer = CommentSerializer(comments, many=True)
    return Response({ "data": serializer.data })
```

ให้เราทำการลองเล่น API Get Comments ที่ endpoint `/posts/10/comments` ด้วย Postman ดู

<br><hr><br>

## Exercise

จากนั้นลองมาดู API get all posts กันบ้าง ให้เราใช้ PostSerializer ในการ serialize ข้อมูลออกไปใน response

<details>
<summary>แอบดูเฉลย</summary>
<p>

```python
 @api_view(['GET'])
 @csrf_exempt
 def post_list(request):

   if (request.method == "GET"):
     posts = Post.objects.all()
     serializer = PostSerializer(posts, many=True)
     return Response({ "data": serializer.data })

```

</p>
</details>

<br><hr><br>

## Create Post Serilizer

ต่อไปเราจะมาดู API ที่ใช้สร้าง Post กันว่าเราจะใช้ประโยชน์จาก serializer ยังไงได้บ้าง

```python
if (request.method == "POST"):
  serializer = PostSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response({ "message": "created post successfully." }, status=status.HTTP_201_CREATED)

  return Response({ "message": "created post failed", "errors": serializer.errors }, status=status.HTTP_400_BAD_REQUEST)
```

- เราจะใช้ PostSerializer ในการ serialize ตัวข้อมูลที่ส่งเข้ามา เราจะส่ง `request.data` เข้าไปใน PostSerializer
- จากนั้นเราจะทำการ validate ข้อมูลด้วย `serializer.is_valid()`
- ถ้าข้อมูลของเราถูกต้องเราจะ save ข้อมูลลง db `serializer.save()`
- จากนั้นเราจะ return response success ออกไป พร้อม `status.HTTP_201_CREATED`
- ถ้าข้อมูลเราผิดเราจะ return response failed ออกไป พร้อม `status.HTTP_400_BAD_REQUEST`

อย่าลืมใส่ `@api_view(['GET', 'POST'])` ด้วยนะ

<br><hr><br>

## Refactor Other APIs

เราจะมา refactor code ของ APIs ตัวอื่น ๆ ที่เหลือกัน

APIs ที่เหลือ

- get post by id
- update post
- delete post

<br><hr><br>

## Exercise

ให้ลอง Refactor API get post by id โดยใช้ PostSerializer

<details>
<summary>แอบดูเฉลย</summary>
<p>

```python
@api_view(['GET'])
    @csrf_exempt
    def single_post_detail(request, post_id):
      if request.method == "GET":
        try:
          post = Post.objects.filter(id=post_id)
          serializer = PostSerializer(post[0])
          return Response({ "data": serializer.data })
        except:
          return Response({ "data": {} }, status=status.HTTP_404_NOT_FOUND)
```

</p>
</details>

<br><hr><br>

## Refactor Update Post API

```python
 if request.method == "PUT":
    try:
      queried_post = Post.objects.filter(id=post_id)[0]
      serializer = PostSerializer(post, data=request.data)

      if serializer.is_valid():
        serializer.save()
        return Response({ "message": "updated post successfully." })
      return Response({ "message": "updated post failed", "errors": serializer.errors }, status=status.HTTP_400_BAD_REQUEST)

    except IndexError:
      return Response({ "message": "post not found" }, status=status.HTTP_404_NOT_FOUND)
```

อย่าลืมใส่ http method `PUT` เข้าไปใน api_view decorator ด้วย

<br><hr><br>

## Refactor Delete Post API

```python
if request.method == "DELETE":
    try:
      post = Post.objects.filter(id=post_id)[0]
      post.delete()
      return Response({ "message": "deleted post successfully." })
    except IndexError:
      return Response({ "message": "post not found" }, status=status.HTTP_404_NOT_FOUND)
```

<br><hr><br>

## Last Refactor

เราจะสังเกตได้ว่า post = Post.objects.filter(id=post_id) มันซ้ำกันค่อนข้างมาก เราจะ refactor ตรงนี้ให้มันไม่ซ้ำซ้อนกันซักหน่อย

```python
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def single_post_detail(request, post_id):
  post = Post.objects.filter(id=post_id)

  if not len(post):
    return Response({ "message": f"post {post_id} not found" }, status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = PostSerializer(post[0])
    return Response({ "data": serializer.data })


  if request.method == "PUT":
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({ "message": "updated post successfully." })
    return Response({ "message": "updated post failed", "errors": serializer.errors }, status=status.HTTP_400_BAD_REQUEST)

  if request.method == "DELETE":
    post.delete()
    return Response({ "message": "deleted post successfully." })

```

# ORM With Relations

เรามาลองสร้าง Relation ของ Models กัน โจทย์คือ 1 Post มีได้หลาย ๆ Comments

เราจะแก้ `blogs/models.py` ได้แบบนี้

```python
from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=150)
  content = models.CharField(max_length=2000)

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  comment = models.TextField()
  created_on = models.DateTimeField()
  updated_on = models.DateTimeField(auto_now=True)

  class Meta:
   db_table = "comments"
```

- Comment model จะมี property post ที่เป็น Foreign Key ของตัว Post model
- เราจะกำหนดว่า เมื่อ Post​โดนลบ Comments ที่ผูกกับ Post นั้น ๆ อยู่จะถูกลบไปด้วย `on_delete=models.CASCADE`
- จากนั้นเราจะมี Sub-class ที่ชื่อว่า Meta เป็น class ที่ทำให้เราสามารถกำหนดลูกเล่นได้เวลาเราสร้าง Table ในที่นี้เราจะกำหนดชื่อของตารางด้วย `db_table` property

เมื่อเราเปลี่ยนแปลง Models ของเราให้เราทำการ makemigrations ใหม่ และ migrate ตารางใหม่ลง database

`python myproject/manage.py makemigrations --name add_comment_model blogs`

`python myproject/manage.py migrate`

<br><hr><br>

## Interacting With Models On Shell

เราจะมาทดลองใช้ ORM จาก Python Shell ให้เราเปิด shell จาก manage.py

`python myproject/manage.py shell`

จากนั้นให้เรา import models Post, Comment จาก blogs.models

```python
from blogs.models import Post, Comment
from datetime import datetime
```

จากนั้นเราจะสร้าง Post และ Comment ด้วย ORM

```python
post = Post(title="post with comment", content="post comment")
comment = Comment(post=post, comment="comment on post", created_on=datetime.now(), updated_on=datetime.now())
```

เราสามารถ Save Post และ Comment ลง DB ผ่าน `save()`

```python
post.save()
comment.save()
```

เราสามารถดึงข้อมูล Post จาก Comment ได้

```python
comment.post
comment.post.title
comment.post.content
```

เราสามารถที่จะดึงข้อมูล Comments ของ Post นั้น ๆ ออกมาได้แบบนี้

```python
comments = Comment.objects.filter(post_id=9)
comments.values()
comments.values()[0]
comments.values()[1]
```

<br><hr><br>

## Building Comment APIs

เราจะสร้าง API ที่เอาไว้ดึงข้อมูลของ Comments จาก Post นั้น ๆ

หน้าตา Endpoint ของเราจะเป็นแบบนี้ `/posts/<str:post_id>/comments`

เราจะมาเริ่มสร้าง function เอาไว้รับ request ก่อน

```python
def comment_list(request, post_id):
  if (request.method == "GET"):
    queried_comments = Comment.objects.filter(post_id=post_id)

    data = list(queried_comments.values())

    response_data = {}
    response_data['data'] = data

    response = JsonResponse(response_data)

    response.status_code = 200
    return response
```

- เราจะสร้าง function `comment_list` จะมี params เป็น request และ post_id
- จากนั้นเราจะใช้ ORM ในการหา Comments ของ Post นั้น ๆ `Comment.objects.filter(post_id=post_id)`
- ต่อไปเราจะ get values ที่อยู่ใน Comment Object ออกมา แล้วเปลี่ยนเป็น list
- จากนั้นเราจะ return response พร้อม Comments ออกไป

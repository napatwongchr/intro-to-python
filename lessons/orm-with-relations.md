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
```

- Comment model จะมี property post ที่เป็น Foreign Key ของตัว Post model
- เราจะกำหนดว่า เมื่อ Post​โดนลบ Comments ที่ผูกกับ Post นั้น ๆ อยู่จะถูกลบไปด้วย `on_delete=models.CASCADE`

เมื่อเราเปลี่ยนแปลง Models ของเราให้เราทำการ makemigrations ใหม่ และ migrate ตารางใหม่ลง database

`python myproject/manage.py makemigrations`

`python myproject/manage.py migrate`

## Interacting With Models On Shell

เราจะมาทดลองใช้ ORM จาก Python Shell ให้เราเปิด shell จาก manage.py

`python myproject/manage.py shell`

จากนั้นให้เรา import models Post, Comment จาก blogs.models

```python
from blogs.models import Post, Comment
```

จากนั้นเราจะสร้าง Post และ Comment ด้วย ORM

```python
post = Post(title="post with comment", content="post comment")
comment = Comment(post=post, comment="comment on post")
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

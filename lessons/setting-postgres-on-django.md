# Setting Postgres On Django

1. Start postgres ก่อน

2. จากนั้นแก้ไฟล์ `myproject/settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

3. จากนั้นเราต้องทำการ install psycopg2 ด้วย `python -m pip install psycopg2`

   - ใน Mac ถ้า install psycopg2 ไม่ได้ ให้ ลง psycopg2-binary แทน

4. Run คำสั่ง makemigrations ก่อน ด้วย `python myproject/manage.py makemigrations`

   - **makemigrations** เป็นคำสั่งที่ update และตรวจสอบ ตัว history หรือ transaction ของตัว table ของเรา เราจะ run คำสั่งนี้ทุกครั้งที่เรามีการเปลี่ยนแปลง Model

   - **migrate** เป็นคำสั่งที่จะ submit ตัว table เข้าไปใน database จริง ๆ

ถ้าเรา run makemigrations เราจะเจอ text แบบนี้ เนื่องจากเรายังไม่ได้มีการเปลี่ยนแปลง models ใน Django เลย

```
No changes detected
```

เรามา migrate กัน ด้วยคำสั่ง `python myproject/manage.py migrate` เราจะเจอข้อความแบบนี้

```
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
```

ให้เราลองไปดู postgres เราจะเห็นตาราง ที่เรา migrate เข้าไป

จากนั้นเราจะมาสร้าง model เพื่อสร้าง ตารางใหม่เข้าไปใน db กัน ให้เราไปที่ `posts/models.py` แล้วเขียน model ขึ้นมาตามนี้

```python
from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=150)
  content = models.CharField(max_length=2000)
```

เมื่อเราเขียน model เสร็จแล้วอย่าลืม ใส่ posts app เข้าไปใน INSTALLED_APPS ด้วย

```python
INSTALLED_APPS = [
    'posts.apps.PostsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

จากนั้นทำการ makemigration ใหม่อีกรอบ `python myproject/manage.py makemigrations` เนื่องจาก model ของเราเปลี่ยนแปลง

```
Migrations for 'posts':
  myproject/posts/migrations/0001_initial.py
    - Create model Post
```

เมื่อ makemigration เสร็จแล้วให้เราทำการ migrate

```
  Apply all migrations: admin, auth, contenttypes, posts, sessions
Running migrations:
  Applying posts.0001_initial... OK
```

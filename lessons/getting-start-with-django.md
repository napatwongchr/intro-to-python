# Getting Start With Django

Django เป็น Web framework ที่ใช้ช่วยพัฒนา Web applications

Slogan “The web framework for perfectionists with deadlines”

Code ทั้งหมดที่จะลองทำให้ดูอยู่ https://github.com/napatwongchr/python-blog-app

## Why Django ?

1. Ridiculously fast - Learning curve ต่ำ ช่วยให้เราพัฒนา Application ได้ไวมากตาม Slogan ของเค้าเอง
2. Fully loaded with tools - เครื่องมือพร้อมในตัว ทำให้เราทำงานได้ง่าย และไวมากยิ่งขึ้น
3. Reassuringly secure - มีความปลอดภัยสูง
4. Exceedingly scalable - ง่ายต่อการ Scale ระบบ
5. Incredibly versatile - Django สามารถใช้ได้กับ application ได้หลากหลายรูปแบบ เช่น CMS, Social Network, หรือ พวกระบบการคำนวณทางวิทยาศาสตร์ ต่าง ๆ

## Setup django project

1. สร้าง project folder python-blog-app

2. จากนั้น cd python-blog-app

3. ต่อไปให้ทำการสร้าง folder backend ขึ้นมาเพื่อเก็บ source code ของ backend ไว้

4. จากนั้น cd เข้าไปที่ backend folder

5. ให้เราทำการสร้าง virtual environment ขึ้นมา `python -m venv env`

6. ให้เราทำการ activate virtual environment

   - ใน MacOS env/bin/activate
   - ใน Windows env/Scripts/activate

7. จากนั้นให้ทำการ install django ด้วย `python -m pip install django`
8. ให้เราเช็คว่า django ที่เรา installed ไป เสร็จสมบูรณ์ด้วย `python -m django --version`

9. จากนั้นให้เราทำการสร้าง project ของเราด้วย

`django-admin startproject myproject`

ภายใน project จะมีไฟล์ต่าง ๆ มากมายให้เราลองมาไล่ดูทีละไฟล์

**myproject** — (**ข้างนอกสุด**) เป็นเหมือน Folder container ไว้คลุมตัว Django Project เฉยๆ <br>

**manage.py** — ไฟล์ที่ทำให้เราจัดการ Django Project ได้หลายอย่าง เช่น การเปิด development server <br>

**myproject **— (**ข้างในอีกชั้น**) เป็น Python package folder เราสามารถ import files functions ต่างๆ ที่อยู่ในนี้ได้ เช่น mysite.urls <br>

mysite/**init**.py — เป็นไฟล์เปล่า ๆ ที่บอกว่า Folder นี้จะเป็น Python packages <br>

mysite/**urls**.py — url ต่างใน project ของเราจะถูก Define ไว้ที่นี่ <br>

mysite/**asgi**.py และ mysite/**wsgi**.py — เป็นไฟล์ที่ใช้จัดการ Deployment <br>

10. จากนั้นให้ทำการ run project ขึ้นมาด้วย

`python myproject/manage.py runserver`

เราจะเห็นข้อความแบบนี้ใน Terminal เป็นข้อความเตือนเรื่องของ migration

```
System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 11, 2021 - 13:57:43
Django version 3.1.7, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C
```

จากนั้นให้เราลองเข้าไปที่ http://127.0.0.1:8000/ ดูเราจะเห็นหน้าเว็บเริ่มต้นที่ถูกสร้างไว้ด้วย django

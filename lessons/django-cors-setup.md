# Django CORS Setup

Cross-origin resource sharing (CORS) เป็น กลไกลของ Web browser ที่จะทำให้เราสามารถควบคุมการเข้าถึง resources ที่อยู่นอก domain ที่เรากำหนดได้

ข้อดีของ CORS คือทำให้ application ของเรามีความปลอดภัยมากยิ่งขึ้น

## Start Setup CORS on Django

1. ทำการ Install package django-cors-headers

`python -m pip install django-cors-headers`

2. ใส่ `corsheaders` เข้าไปที่ list INSTALLED_APPS ในไฟล์ `settings.py`

```
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]
```

3. ใส่ `'corsheaders.middleware.CorsMiddleware'` เข้าไปที่ list MIDDLEWARE ในไฟล์ `settings.py`

- _อย่าลืม comma_
- _เช็คให้ดี ใส่ข้างบน 'django.middleware.common.CommonMiddleware'_

```
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
```

4. ใส่ domain ของ application ที่เราจะ allow ถ้า frontend เราอยู่ที่ `localhost:3000` ก็ใส่เข้าไป

```
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000"
]
```

5. ลอง Test call api จาก frontend

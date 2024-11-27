## Setup

```python
# Create project folder
mkdir my_projects

# Create a virtual environment (Windows)
py -m venv myvenv

# Activate virtual environment (Windows)
myvenv\Scripts\activate.bat

# Create a virtual environment (MacOS)
python3 -m venv myvenv

# Activate virtual environment (MacOS)
source myvenv/bin/activate

pip install django

# Create project "myblogs"
django-admin startproject myblogs

# Create the "blogs" app
python manage.py startapp blogs
```

> ติดตั้ง Potgres Client `psycopg2` ติดตั้ง `django-extensions` และ `jupyter notebook` ด้วยคำสั่ง
> 

```python
pip install psycopg2

pip install psycopg2-binary

pip install django-extensions ipython jupyter notebook

pip install ipython==8.25.0 jupyter_server==2.14.1 jupyterlab==4.2.2 jupyterlab_server==2.27.2

pip install notebook==6.5.6
#หากติดตั้ง หรือ run jupyter ไม่ได้ให้ลองเปลี่ยน notebook version ดังนี้ 6.5.7

```

จากนั้นสร้าง directory ชื่อ `notebooks`

```
mkdir notebooks
```

> **DB ใน postgres แก้ใน setting.py**
> 

```
# Database setting
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "myapp",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# Add app blogs to INSTALLED_APPS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Add your apps here
    "django_extensions",
    "blogs",
]
```

> makemigrations เพื่อให้ Django ทำการสร้างไฟล์ migration ขึ้นมา
> 

```python
python manage.py makemigrations
python manage.py migrate
```

ทำการ start Jupyter Notebook server ด้วย command

```
python manage.py shell_plus --notebook
```

ใน Cell แรกของไฟล์ Notebook เพิ่ม code นี้ลงไป

```python
import os
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
```


### คำแนะนำการติดตั้งทีละขั้นตอน tailwind

1. ติดตั้งแพ็กเกจ **django-tailwind** ผ่าน pip:
    
    ```bash
    python -m pip install django-tailwind
    ```
    
2. ถ้าคุณต้องการให้หน้าเว็บโหลดใหม่อัตโนมัติระหว่างการพัฒนา (ดูขั้นตอนที่ 10-12 ด้านล่าง) ให้ใช้ extras [reload] ซึ่งจะติดตั้งแพ็กเกจ **django-browser-reload** ด้วย:
    
    ```bash
    python -m pip install 'django-tailwind[reload]'
    ```
    
3. หรือคุณสามารถติดตั้งเวอร์ชันล่าสุดที่กำลังพัฒนาได้จาก:
    
    ```bash
    
    python -m pip install git+https://github.com/timonweb/django-tailwind.git
    ```
    
4. เพิ่ม `'tailwind'` ใน `INSTALLED_APPS` ในไฟล์ `settings.py`:
    
    ```python
    
    INSTALLED_APPS = [
      # แอปของ Django อื่นๆ
      'tailwind',
    ]
    ```
    
5. สร้างแอป Django ที่ใช้ร่วมกับ Tailwind CSS โดยใช้คำสั่ง:
    
    ```bash
    python manage.py tailwind init
    ```
    
6. เพิ่มแอปใหม่ `'theme'` ที่คุณสร้างลงใน `INSTALLED_APPS` ในไฟล์ `settings.py`:
    
    ```python
    
    INSTALLED_APPS = [
      # แอปของ Django อื่นๆ
      'tailwind',
      'theme',
    ]
    ```
    
7. ลงทะเบียนแอป `'theme'` ที่สร้างขึ้นโดยเพิ่มบรรทัดต่อไปนี้ในไฟล์ `settings.py`:
    
    ```python
    TAILWIND_APP_NAME = 'theme'
    ```
    
8. ตรวจสอบให้แน่ใจว่าได้มีการเพิ่มรายการ `INTERNAL_IPS` และมีที่อยู่ IP 127.0.0.1 ในไฟล์ `settings.py`:
    
    ```python
    INTERNAL_IPS = [
        "127.0.0.1",
    ]
    ```
    
9. ติดตั้ง dependencies ของ Tailwind CSS โดยใช้คำสั่ง:
    
    ```bash
    
    python manage.py tailwind install
    
    ```
    
10. **Django Tailwind** มาพร้อมกับ template `base.html` ที่อยู่ในโฟลเดอร์ `your_tailwind_app_name/templates/base.html` คุณสามารถขยายหรือลบได้ถ้าคุณมี layout ของคุณเองแล้ว
11. ถ้าคุณไม่ได้ใช้ template `base.html` ที่มาพร้อมกับ Django Tailwind ให้เพิ่ม `{% tailwind_css %}` ลงใน template `base.html` ของคุณ:
    
    ```html
    {% load static tailwind_tags %}
    <head>
        ...
        {% tailwind_css %}
        ...
    </head>
    ```
    
12. เพิ่มและตั้งค่า **django_browser_reload** ซึ่งจะช่วยให้หน้าเว็บโหลดใหม่อัตโนมัติในโหมดการพัฒนา เพิ่มมันใน `INSTALLED_APPS` ในไฟล์ `settings.py`:
    
    ```python
    INSTALLED_APPS = [
      # แอปของ Django อื่นๆ
      'tailwind',
      'theme',
      'django_browser_reload',
    ]
    ```
    
13. เพิ่ม middleware ใน `settings.py`:
    
    ```python
    MIDDLEWARE = [
      # ...
      "django_browser_reload.middleware.BrowserReloadMiddleware",
      # ...
    ]
    ```
    
    **หมายเหตุ:** ควรวาง middleware นี้หลัง middleware ที่มีการเข้ารหัส response เช่น `GZipMiddleware` ของ Django
    
14. รวม URL ของ **django_browser_reload** ในไฟล์ `urls.py`:
    
    ```python
    
    from django.urls import include, path
    urlpatterns = [
        ...,
        path("__reload__/", include("django_browser_reload.urls")),
    ]
    ```
    
15. สุดท้าย คุณสามารถใช้คลาส Tailwind CSS ใน HTML ของคุณได้แล้ว เริ่มเซิร์ฟเวอร์พัฒนาโดยรันคำสั่ง:
    
    ```bash
    
    python manage.py tailwind start
    ```
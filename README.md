# Pelatihan WebAcademy INFEST 6.0

Pelatihan Python dan Django bagi pemula

### <1> Buat Project Django

```
  (env)$ django-admin startproject <nama projek> (<direktori>)
```

### <2> Menambahkan tabel ke database

```
 (env)$ python manage.py migrate
```

### <3> Jalankan localserver

```
 (env)$ python manage.py runserver
```

### <4> Membuat app

```
 (env)$ python manage.py startapp <nama app>
```

### <5> Membuat akun superuser

```
 (env)$ python manage.py createsuperuser
```

### <6> Menangkap perubahan model dari app

```
 (env)$ python manage.py makemigrations
```

## Instalasi

1. Download [python](https://www.python.org/) dan install
2. Install virtualenv
```
      $ pip install virtualenv
```
3. Buat virtualenv
```
      $ virtualenv env
```
4. Aktivasi virtual environment python
```
      $ env\Script\activate
```
5. Install django dan pillow
```
 (env)$ pip install django pillow
```

## Membuat projek awal

Lakukan langkah <1> <2> <5> <3> secara berurutan

## Membuat model

Lakukan langkah <6> <2>

## Sumber refensi

- [django](https://docs.djangoproject.com/en/3.1/)
- [Class Based View](http://ccbv.co.uk/)

# django-blog
A Blog with Django Framework

# Installation
> this project is using PostgreSQL DataBase. so you must config your DataBase from **_./blog/blog/settings.py.sample/DATABASES_** before DB migrations.
> note that rename **_./blog/blog/settings.py.sample/_** to **_./blog/blog/settings.py/_** (REMOVE 'sample')
### install and create your virtual environment

install virtualenv:
```
pip install virtualenv
```

create virtual environment:
```
virtualenv venv
```

activate virtual environment:
```
cd venv\Scripts\activate
```

if you using Widows PowerShell, type this command in your PowerShell before activate virtual environment:
```
Set-ExecutionPolicy Unrestricted -Scope Process
```

### install requirements and run project

install requirements:
```
pip install -r requirements.txt
```

preparing DataBase:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
```

create super user for access to admin section:
```
python3 manage.py createsuperuser
```
*fill necessary fields*

run project on localhost (default port: 8000):
```
python3 manage.py runserver <port>
```


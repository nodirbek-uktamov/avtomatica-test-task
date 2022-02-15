## About project:
Database: PostgreSQL  
Python version: 3.9  
Django version: 3.0.5  
Django rest framework version: 3.10.3  



###database settings (linux / mac):
```commandline
createdb nodirbek_task_django
```

open `config.settings_dev.py` and change 
1. USER
2. PASSWORD  
if you created db with another name, write it to `NAME` field

or in windows open pgAdmin and create db with name `nodirbek_task_django`


##running project:
```commandline
mkvirtualenv some_unique_name_for_virtual_env  
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### *you can use postman or api in browser*

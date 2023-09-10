# MML BACKEND

This repository contains MyMusicList BACKEND code.

## Requirements
- Python 3+
- Mysql


## Before installation
 - Install requirements 
 - Create an empty database for project (i suggest MariaDB for database management)
 
 
## Json example
``` 
{
    "SECRET_KEY":"insert_key",
    "DATABASES":{
            "default":{
                "ENGINE":"django.db.backends.mysql",
                "NAME": "insert_name",
                "USER": "insert_user",
                "PASSWORD":"insert_password",
                "HOST": "insert_host", 
                "PORT": "insert_port"
            }
    },
    "STATICFILES_DIRS":"C:/var/"insert_name",
    "STATIC_ROOT":"/var/www/spasiic/static/",
    "MEDIA_ROOT":"/var/www/spasiic/media/"
}
```

## Installation

``` bash
git clone https://github.com/Spasiic/backend.git # Clone repo
python -m venv venv  # Create virtual enviroment for dependencies
./venv/scripts/activate  # Start virtual enviroment

cd backend
cd core 
#CREATE a file called '.env' with your credentials inside following ENV example section or ask a senior developer for his .env file.
cd ..

pip install -r requirements.txt  # Install dependecies
python manage.py makemigrations
python manage.py migrate
python manage.py runserver localhost:80 # or 127.0.0.1:80 to expose for public, you also need port forwaded 80.
# SERVER IS RUNNING
```
## Features

- Models: profile (Profile), music (Artist, Album, Music); misc (WishListEntry, Alarm)
- Endpoints for: authentication of the user (CRUD user + profile); CRUD for Artists, albums and musics; CRUD for wishListEntries and alarms.
- Others...

Install the depedencies and run the code, have fun!

## License

**This isn't a Free Software, Hell nahh!**

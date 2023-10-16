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
    "DEBUG":true,
    "DATABASES":{
            "default":{
                "ENGINE":"django.db.backends.mysql",
                "NAME": "insert_database_name",
                "USER": "insert_database_user",
                "PASSWORD":"insert_database_password",
                "HOST": "insert_database_host", 
                "PORT": "insert_database_port"
            }
    },
    "TIME_ZONE":"America/Fortaleza",
    "USE_TZ":false,
    "STATICFILES_DIRS":"/home/kosolov325/mymusiclist/static",
    "STATIC_ROOT":"/var/www/mymusiclist/static/",
    "MEDIA_ROOT":"/var/www/mymusiclist/media/",
    "ALLOWED_HOSTS":["*"],
    "CORS_ALLOWED_ORIGINS":[],
    "CORS_ALLOW_ALL_ORIGINS":true
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

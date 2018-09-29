# Moviemancer

Moviemancer is a website for movie recommendation.
**Production:** http://moviemancer-api.herokuapp.com/

![Moviemancer in action](https://im4.ezgif.com/tmp/ezgif-4-4ab46b2765.gif)

## Getting Started

### Requirements

- [Python 2.7](https://www.python.org/downloads/release/python-2715/)
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

## Instalation

- `$ pipenv install`

## Running Locally

### Setting the Database

#### Restoring the backup

*`Attention:` The following steps require access to the aplication on Heroku*

```
$ heroku pg:backups:download
$ pg_restore --verbose --clean --no-acl --no-owner -h localhost -U myuser -d mydb latest.dump
```

#### Configuring settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'mydb',  
        'USER': 'myuser',
        'PASSWORD': ******,
        'HOST': 'localhost',  
        'PORT': 5432, 
    }
}
```

### Runing

- `$ make run`
- open `http://127.0.0.1:8000`

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```

or
[![Deploy](https://www.herokucdn.com/deploy/but
[![Coverage Status](https://coveralls.io/repos/github/betinacosta/moviemancer/badge.svg?branch=master)](https://coveralls.io/github/betinacosta/moviemancer?branch=master)
[![Build Status](https://travis-ci.com/betinacosta/moviemancer.svg?branch=master)](https://travis-ci.com/betinacosta/moviemancer)

# Moviemancer

Moviemancer is a website for movie recommendation.

**Production:** http://moviemancer-api.herokuapp.com/

![moviemancer on action](https://media.giphy.com/media/WQNBEWPkChL6WV0FRM/giphy.gif)

## Getting Started

### Requirements

- [Python 3.6.5](https://www.python.org/downloads/release/python-2715/)
- [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

## Instalation

- `$ make setup`

## Running Locally

### Setting the Database

Inside the project directory run: `$ make recreate_db`

This will drop the moviemancer database and user in case you already have one and recreate those with the proper configuration.

If you wish just setup a moviemancer db that you already created, just run `$ make setup_db`

#### Configuring settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'moviemancer',
        'USER': 'moviemancer',
        'PASSWORD': moviemancer,
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
```

### Runing

Inside the project directory run:

- `$ make run`
- open `http://127.0.0.1:8000`

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```

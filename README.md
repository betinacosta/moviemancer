# Moviemancer

Moviemancer is a website for movie recommendation.

# Getting Started

## Requirements

- Python 2.7
- pip
- PostgreSQL

## Instalation

- Inside the project run `pip install -r requirements.txt`;

## Running Locally

### Requirements

- [Heroku Toolbelt](https://toolbelt.heroku.com/)

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

# Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
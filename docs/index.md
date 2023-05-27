# bobotog-news

[![Build Status](https://travis-ci.org/sevbo2003/bobotog-news.svg?branch=master)](https://travis-ci.org/sevbo2003/bobotog-news)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

News backend for Bobotog'. Check out the project's [documentation](http://sevbo2003.github.io/bobotog-news/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```

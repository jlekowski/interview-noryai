# Nory Weird Salads Django Bootstrap

This repo contains a starting point for the Nory Weird Salads interview challenge using the [Django](https://www.djangoproject.com/) framework.

This project is intended to help you get started quickly, minimizing the time spent setting up a development environment.

Choose this starting point if you are comfortable using Django for implementing web applications.

## Using uv and Python

Once [uv](https://docs.astral.sh/uv/) is installed most commands will run out of the box using `uv run ...` as a prefix.

For example:
```sh
# Ensure everything needed is installed
uv sync

# Add dependencies
uv add django

# e.g. python manage.py makemigrations becomes:
uv run python manage.py makemigrations

# e.g. running tests
uv run python manage.py test
uv run pytest

# e.g. running django admin commands
uv run python manage.py startapp myapp
uv run python manage.py migrate
uv run python manage.py runserver
```

To create migrations:
```sh
uv run python manage.py makemigrations
```

## Using Docker

To start in Docker:
```sh
docker compose run --build web django-admin migrate
docker compose up --build --watch
```

The Django app will be available on [http://localhost:8000/](http://localhost:8000/).

Docker will watch for changes and trigger reloads or rebuilds of the app as needed.


To apply migrations:
```sh
docker compose exec web django-admin migrate
```

To create an admin user:
```sh
docker compose exec web django-admin createsuperuser
```

# Notes

This does not have all the models implemented, that's for you to do! In fact, the models which are implemented might not be ideal, feel free to change.

This project uses [uv](https://docs.astral.sh/uv/) to manage dependencies.

Docker is used to run and develop the project out of the box if you don't want to run python directly. This project follows the [uv Docker](https://docs.astral.sh/uv/guides/integration/docker/) integration guide.

This project was created using:
```sh
uv init
uv add django psycopg[binary,pool] pyyaml
uv add --dev ruff mypy django-stubs
uv run django-admin startproject weird_salads_site .
uv run django-admin startapp weird_salads
uv run django-admin startapp weird_salads_staff
```

There are currently three packages:
1. [weird_salads_site](./weird_salads_site/) - the Django site configuration.
2. [weird_salads](./weird_salads/) - Weird Salads itself, top level routes and views.
3. [weird_salads_staff](./weird_salads_staff/) - An example model for Staff and related views.

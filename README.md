[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

# FastAPI & PostgreSQL - Starter Template

This template is initialised with minimal configurations, the main purpose is to allow beginners to get comfortable with FastAPI and hit the ground running.

## Usage

### Dependencies

You will need the following dependencies to run or contribute to this project:

- [Python3](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

### Getting started with docker

To run

```
docker-compose build
docker-compose up
```

Access docs at http://localhost:8080/docs/

Access pgAdmin at http://localhost:5050/

To shutdown

```
docker-compose down
```

---

#### Migrations

```
docker-compose run app alembic revision --autogenerate -m "version_"
```

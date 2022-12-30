# :strawberry: Fastapi with graphql

Fastapi api with GraphQL using Strawberry

## :floppy_disk: Installation

```bash
python -m venv env
```

```bash
. env/scripts/activate
```

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

## :wrench: Config

Create `.env` file. Check the example `.env.example`

:lock: How to create a secret key:

```bash
openssl rand -base64 64
```

:construction: Before first run:

Run `docker-compose` :whale: to start the database server

```bash
docker compose -f "docker-compose.yml" up -d --build adminer db
```

and init the database with alembic:

```bash
alembic upgrade head
```

## :runner: Run

```bash
uvicorn app.main:app --reload
```

## :pushpin: Features

- Basic login
- Create users and posts
- Examples endpoints CRUD
- GraphQL endpoint

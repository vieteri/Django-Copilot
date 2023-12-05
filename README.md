# Django-Copilot

Django-Copilot is a web application built with Django.

## Installation
1. Clone the repository:
2. Install the requirements:
Docker
3. Create .env file for db
```python
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
DB_PORT=5432
```
## Usage

### Containers

1. Create docker image:
docker-compose build
docker compose up
2. Start the server:
docker compose up


#### Django
1. Make the migrations
```bash
docker exec [image_name_web] python3 mysite/manage.py makemigrations
docker exec [image_name_web] python3 mysite/manage.py migrate
```
2. Open your web browser and navigate to `http://127.0.0.1:8000/`

#### PG-Admin

1. Open your web browser and navigate to `http://127.0.0.1:5050/`

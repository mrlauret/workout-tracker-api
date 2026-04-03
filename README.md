# workout-tracker-api

A REST API for tracking workouts built with Django and Django REST Framework. Users can create custom exercises, log workouts, and track sets and reps per session. Full JWT authentication included.

## Stack

- **Django 6.0.3** — web framework
- **Django REST Framework** — API layer
- **SimpleJWT** — JWT authentication
- **PostgreSQL** — database
- **django-cors-headers** — CORS support for frontend integration

## Features

- Custom user model with username-based authentication
- JWT authentication with access and refresh tokens
- User-specific exercises — each user builds their own exercise library
- Full workout logging with sets and reps per exercise
- All data is private — users can only access their own workouts and exercises
- Nested serializers — exercise names returned instead of raw IDs

## Data Model

```
User
 ├── Workout (ForeignKey → User)
 │    └── WorkoutExercise (through table)
 │         ├── sets (int)
 │         └── repetitions (int)
 └── Exercise (ForeignKey → User)
      └── WorkoutExercise (ForeignKey → Exercise)
```

- A `User` owns many `Workouts` and many `Exercises`
- A `Workout` contains many `Exercises` through the `WorkoutExercise` table
- The same `Exercise` can appear in many `Workouts` with different sets and reps each time

## Project Structure

```
core/
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── workouts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/MrLauret/workout-tracker-api.git
cd workout-tracker-api
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create PostgreSQL database

```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE db;
CREATE USER admin WITH PASSWORD '1234';
GRANT ALL PRIVILEGES ON DATABASE db TO admin;
\q
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the server

```bash
python manage.py runserver
```

API will be available at `http://localhost:8000`.

## Endpoints

### Auth

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| POST | `/api/users/register/` | No | Create account |
| POST | `/api/users/login/` | No | Get access + refresh tokens |
| POST | `/api/users/token/refresh/` | No | Refresh access token |
| GET | `/api/users/profile/` | Yes | Get current user |

### Exercises

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| GET | `/api/exercises/` | Yes | List your exercises |
| POST | `/api/exercises/` | Yes | Create an exercise |
| DELETE | `/api/exercises/<id>/` | Yes | Delete an exercise |

### Workouts

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| GET | `/api/workouts/` | Yes | List your workouts |
| POST | `/api/workouts/` | Yes | Create a workout |
| DELETE | `/api/workouts/<id>/` | Yes | Delete a workout |

### Workout Exercises

| Method | URL | Auth | Description |
|--------|-----|------|-------------|
| GET | `/api/workouts/<id>/exercises/` | Yes | List exercises in a workout |
| POST | `/api/workouts/<id>/exercises/` | Yes | Add exercise to a workout |
| DELETE | `/api/workouts/<workout_id>/exercises/<id>/` | Yes | Remove exercise from workout |

## Usage

### Register

```bash
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "lau", "password": "securepass123"}'
```

### Login

```bash
curl -X POST http://localhost:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "lau", "password": "securepass123"}'
```

Response:

```json
{
    "access": "eyJhbGci...",
    "refresh": "eyJhbGci..."
}
```

### Create an exercise

```bash
curl -X POST http://localhost:8000/api/exercises/ \
  -H "Authorization: Bearer eyJhbGci..." \
  -H "Content-Type: application/json" \
  -d '{"name": "Pull ups"}'
```

### Create a workout

```bash
curl -X POST http://localhost:8000/api/workouts/ \
  -H "Authorization: Bearer eyJhbGci..." \
  -H "Content-Type: application/json" \
  -d '{"name": "Monday push"}'
```

### Add exercise to workout

```bash
curl -X POST http://localhost:8000/api/workouts/1/exercises/ \
  -H "Authorization: Bearer eyJhbGci..." \
  -H "Content-Type: application/json" \
  -d '{"exercise_id": 1, "sets": 3, "repetitions": 10}'
```

Response:

```json
{
    "id": 1,
    "workout": 1,
    "exercise": {
        "id": 1,
        "name": "Pull ups"
    },
    "sets": 3,
    "repetitions": 10
}
```

### List exercises in a workout

```bash
curl http://localhost:8000/api/workouts/1/exercises/ \
  -H "Authorization: Bearer eyJhbGci..."
```

### Delete exercise from workout

```bash
curl -X DELETE http://localhost:8000/api/workouts/1/exercises/1/ \
  -H "Authorization: Bearer eyJhbGci..."
```

## Token Lifetime

| Token | Lifetime |
|-------|----------|
| Access | 30 minutes |
| Refresh | 7 days |

## Security Notes

- All endpoints except register and login require a valid JWT token
- Users can only access their own workouts and exercises
- Ownership is enforced at the query level — not just at the permission level
- Passwords are hashed using Django's PBKDF2 algorithm

## Environment Variables

Before deploying, move these out of `settings.py` into a `.env` file:

- `SECRET_KEY`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`

## Notes

- `DEBUG = True` and `ALLOWED_HOSTS = ['*']` are for development only
- CORS is configured for `http://localhost:3000` for local frontend development
- Fully containerized using **Docker** and **Docker Compose**
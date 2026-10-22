# Lessonfy: Configuration

Everything configurable lives in two places: `.env` (local) and the Render dashboard (production). `lessonfy/settings.py` reads them. Never hardcode secrets.

## Environment variables

| Variable | Local `.env` | Render | What it does |
|---|---|---|---|
| `SECRET_KEY` | Generated key | Different generated key | Signs sessions and CSRF tokens. Required. |
| `DEBUG` | `True` | `False` | Shows detailed errors when True. Must be False in production. |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Your Render hostname (added automatically via `RENDER_EXTERNAL_HOSTNAME`) | Which hostnames Django will answer to |
| `DATABASE_URL` | Supabase session pooler string | Same string | Where all data is stored |

If `SECRET_KEY` or `DATABASE_URL` is missing, the app refuses to start and tells you which one.

## Supabase

- Use the **session pooler** string (not the direct connection) in `DATABASE_URL`.
- All tables are created by Django migrations. Never create them by hand in the dashboard.
- After your tables exist (end of Phase 2, step 2.7), turn on **Row Level Security** for each table so they are not exposed through Supabase's public API. Django connects with its own database credentials, so the app keeps working.
- If a connection error mentions SSL, add `?sslmode=require` to the end of `DATABASE_URL`.

## What `settings.py` configures

| Area | Setting | Note |
|---|---|---|
| Secrets | `load_dotenv`, `SECRET_KEY`, `DEBUG` | From `.env` |
| Database | `dj_database_url.parse(DATABASE_URL)` | `conn_max_age=600` reuses connections |
| Templates | `DIRS = [BASE_DIR / "templates"]` | Project-level `templates/` folder |
| Static files | `STATICFILES_DIRS`, `STATIC_ROOT`, WhiteNoise storage | `collectstatic` writes to `staticfiles/` |
| Middleware | WhiteNoise right after `SecurityMiddleware` | Order matters |
| Auth | `LOGIN_URL`, `LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL` | Used from Phase 1 |
| Production hardening | Secure cookies, proxy SSL header | Only active when `DEBUG=False` |

## Step 1.1: the one setting you add yourself

In `lessonfy/settings.py`, uncomment:

```python
AUTH_USER_MODEL = "core.User"
```

Only after the `User` model exists in `core/models.py`, and BEFORE your first `migrate`.

## Deploying to Render (Phase 8)

Create a **Web Service** from your GitHub repo and set:

| Field | Value |
|---|---|
| Build command | `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate` |
| Start command | `gunicorn lessonfy.wsgi` |
| Environment variables | `SECRET_KEY` (new one), `DEBUG=False`, `DATABASE_URL` |

Render's exact labels and defaults change over time, so check its current docs if something looks different. Add variables in the dashboard. Never commit `.env`.

Before deploying, test locally with `DEBUG=False` (step 8.5) to catch static file problems early.

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| "SECRET_KEY is not set" | `.env` missing or not filled in |
| "DATABASE_URL is not set" | Same |
| Password authentication failed | Wrong DB password, or special characters not URL-encoded |
| Can't reach the database | Used the direct string instead of the session pooler, or a typo in the host |
| Styles missing in production | `collectstatic` not run, or WhiteNoise middleware missing |
| `migrate` complains about the user model | You migrated before step 1.1. Reset the Supabase database and redo Phase 1. |

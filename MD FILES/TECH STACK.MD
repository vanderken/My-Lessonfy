# Lessonfy: Tech Stack

The stack is fixed by `AI RULES.MD`. Do not swap any of it without deciding it yourself first.

## At a glance

| Layer | Choice | Why |
|---|---|---|
| Language | Python | Required by the project |
| Web framework | Django | Server-rendered pages, ORM, migrations, built-in auth and admin |
| Frontend | Django templates + HTML + CSS + vanilla JavaScript | No React or other framework |
| Database | Supabase PostgreSQL | Hosted Postgres. Django talks to it directly |
| Authentication | Django built-in auth, custom user model (email login) | NOT Supabase Auth |
| Static files | WhiteNoise | Serves CSS/JS/audio from the Django app on Render |
| Web server | Gunicorn | Production server (`gunicorn lessonfy.wsgi`) |
| Hosting | Render | Deployment target |
| Task tracking | Trello (LESSONFY board) | Phases and checklists |
| Version control | Git + GitHub (`vanderken/My-Lessonfy`) | |

## Python packages (`requirements.txt`)

| Package | What it does here | First needed |
|---|---|---|
| `django` | The framework | Step 0.4 |
| `psycopg[binary]` | Lets Django talk to PostgreSQL (Supabase) | Step 0.8 |
| `python-dotenv` | Loads secrets from `.env` | Step 0.5 |
| `dj-database-url` | Turns the `DATABASE_URL` string into Django database settings | Step 0.8 |
| `whitenoise` | Serves static files in production | Step 8.5 |
| `gunicorn` | Production web server | Step 8.6 |
| `python-docx` | Reads `.docx` files for lesson upload | Step 3.7 |

Per `AI RULES.MD`: explain any new package before installing it, and add it to `requirements.txt`.

## How the pieces connect

```
Browser  <->  Django (views + templates + vanilla JS)  <->  Supabase PostgreSQL
                 |
                 +-- Django auth (sessions, custom email user)
                 +-- WhiteNoise (static files) / Gunicorn (on Render)
```

## What is deliberately NOT used

- Supabase Auth, Supabase JS client, Supabase Storage
- React, Vue, or any frontend framework
- Mobile app, real-time collaboration, spaced repetition, export/print, OCR, external music, AI summaries (see Out of scope in `AI RULES.MD`)

## Database rules in one place

- The Django ORM and migrations are the only source of truth for the schema. Never create tables by hand in the Supabase dashboard.
- Constraints (`CheckConstraint`, `UniqueConstraint`) protect unique email, font size range, line spacing range, valid theme and sound values.
- Row Level Security is turned on in Supabase so tables are not exposed through its public API.
- Every query is scoped to `request.user`.

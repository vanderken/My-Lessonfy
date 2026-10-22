# Lessonfy: Setup (Phase 0)

Follow in order. Tick the matching steps on your Trello Phase 0 card as you go.
Commands show Windows first, then macOS/Linux where they differ.

## 1. Supabase project (steps 0.1 and 0.2)

1. In Supabase, create a new project. Save the **database password** in a password manager.
2. Click **Connect** and copy the **Session pooler** connection string (labels may differ slightly).
3. Replace the password placeholder in that string with your real password. If the password contains `@ : / # ? %`, URL-encode those characters.
4. Keep the string private. Never paste it into chat or commit it.

## 2. Virtual environment and packages (step 0.3)

From inside the `My-Lessonfy` folder:

```
python -m venv venv
```

Activate it:

```
# Windows PowerShell
venv\Scripts\Activate.ps1

# Windows Command Prompt
venv\Scripts\activate.bat

# macOS / Linux
source venv/bin/activate
```

(If PowerShell blocks the script, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once.)

Install:

```
pip install -r requirements.txt
python -m django --version
```

DONE WHEN: the last command prints a version.

## 3. Create your `.env` (step 0.5)

```
# Windows
copy .env.example .env
# macOS / Linux
cp .env.example .env
```

Open `.env` and fill in:
- `SECRET_KEY`: generate one with
  `python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"`
- `DEBUG=True`
- `DATABASE_URL`: your Supabase session pooler string

DONE WHEN: `git status` does NOT list `.env` (it is in `.gitignore`).

## 4. Check the project (steps 0.4 and 0.8)

```
python manage.py check
python manage.py runserver
```

Open http://127.0.0.1:8000/ . You should see: **"Lessonfy is running. Phase 0 setup complete."**

> The Django project (`lessonfy/`) and app (`core/`) are already created in this repo, so you do NOT run `startproject` or `startapp`.

**Do NOT run `python manage.py migrate` yet.** The custom email user model (step 1.1) must be set before the first migrate. If you migrate first, you will have to reset the database.

## 5. First commit (step 0.7)

```
git add .
git commit -m "Phase 0: project skeleton"
git push
```

Check `git status` first: `.env` must not appear.

## Phase 0 finished when

- the page above shows in the browser
- `python manage.py check` passes
- `.env` is not tracked by git
- the repo has your commit

Next: `CONFIGURE.MD` explains every setting. Then start Phase 1 on your Trello board.

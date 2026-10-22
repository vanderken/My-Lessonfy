# Lessonfy: What to Download and Create

Do this once, before `SETUP.MD`. Nothing here needs money.

## 1. Install on your computer

| What | Why | Check it worked |
|---|---|---|
| **Python** (3.10 or newer; check Django's docs for the versions it currently supports) | Runs Django | `python --version` |
| **Git** | Version control, push to GitHub | `git --version` |
| **VS Code** (or any code editor) | Editing | Opens |
| **Chrome** + one other browser (Firefox or Edge) | Testing. Text selection behaves slightly differently between browsers | |

On Windows, tick **"Add Python to PATH"** in the Python installer.

## 2. Create free accounts

| Account | Why |
|---|---|
| **GitHub** | Your repo: `vanderken/My-Lessonfy` |
| **Supabase** | The PostgreSQL database |
| **Render** | Hosting (needed in Phase 8) |
| **Trello** | Your LESSONFY board |

## 3. Get the project

```
git clone https://github.com/vanderken/My-Lessonfy.git
cd My-Lessonfy
```

## 4. Python packages

You do NOT download these by hand. `SETUP.MD` installs them all from `requirements.txt` inside a virtual environment. They are explained in `TECH STACK.MD`.

## 5. Not needed

Node.js, npm, Docker, or a local PostgreSQL install. The database lives in Supabase.

Next: open `SETUP.MD`.

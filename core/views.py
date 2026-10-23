from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.html import escape

from .forms import RegisterForm
from .models import Lesson


@login_required
def home(request):
    # TEMPORARY: kept so the old route still works. Remove in a later step if unused.
    token = get_token(request)
    return HttpResponse(
        f"<p>Logged in as {escape(request.user.email)}</p>"
        f'<form method="post" action="{reverse("logout")}">'
        f'<input type="hidden" name="csrfmiddlewaretoken" value="{token}">'
        '<button type="submit">Log out</button>'
        "</form>"
    )


@login_required
def dashboard(request):
    # Only this user's lessons. Never query Lesson.objects.all() here.
    lessons = Lesson.objects.filter(user=request.user)
    return render(request, "core/dashboard.html", {"lessons": lessons})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
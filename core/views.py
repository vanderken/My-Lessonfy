from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import RegisterForm


def home(request):
    # TEMPORARY: replaced by the real dashboard in step 1.5
    return HttpResponse("Lessonfy is running. Phase 0 setup complete.")


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
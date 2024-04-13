from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        # Process form
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("blogs:index")
    else:
        # New form
        form = UserCreationForm

    return render(request, "registration/register.html", {
        "form": form,
    })
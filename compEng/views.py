# compEng/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth import login
from .forms import UserCreationForm, UserAuthenticationForm
from .models import FacultyUser
from .forms import StudentMarkForm
from .models import StudentMark


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("compEng:home")
        else:
            print(form.errors)
            return render(request, "signup.html", {"form": form})
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


from django.contrib.auth import authenticate, login
from django.http import JsonResponse


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("compEng:home")
        else:
            return render(
                request,
                "login.html",
                {"message": {"success": False, "message": "Invalid login credentials"}},
            )
            # return JsonResponse({'success': False, 'message': 'Invalid login credentials'})
    else:
        return render(request, "login.html")


def landing_view(request):
    return render(request, "landing.html")


def home_view(request):
    if request.method == "POST":
        form = StudentMarkForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentMarkForm()

    # Retrieve all student marks from the database
    student_marks = StudentMark.objects.all()
    user_info = None
    if request.user.is_authenticated:
        user_info = {
            "username": request.user.username,
            "email": request.user.email,
        }

    return render(
        request,
        "home.html",
        {"form": form, "student_marks": student_marks, "user_info": user_info},
    )


def registered_users_view(request):
    users = FacultyUser.objects.all()
    return render(request, "registered_users.html", {"users": users})


def delete_mark_view(request, mark_id):
    mark = get_object_or_404(StudentMark, id=mark_id)
    mark.delete()
    return redirect("compEng:home")


def update_mark_view(request, mark_id):
    mark = get_object_or_404(StudentMark, id=mark_id)

    if request.method == "POST":
        form = StudentMarkForm(request.POST, instance=mark)
        if form.is_valid():
            form.save()
            return redirect("compEng:home")
    else:
        form = StudentMarkForm(instance=mark)

    student_marks = StudentMark.objects.all()

    return render(
        request,
        "home.html",
        {"form": form, "student_marks": student_marks, "selected_mark_id": mark_id},
    )


def logout_view(request):
    logout(request)
    return redirect("compEng:login")

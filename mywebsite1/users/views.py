from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username= username, password = password)
        if user is not None:
            login(request, user)
            return redirect("index")
            #print("로그인 성공")
            # request.session["loginuser"] = user.user_name 
            #return HttpResponseRedirect('blog/templates/index.html')

        else:
            print("로그인 실패")
    # return redirect('index')
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("index")


def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        name = request.POST["name"]
        email = request.POST["email"]

        user = User.objects.create_user(username, email, password)
        user.name = name
        user.save()

        return redirect("user:login")

    return render(request, "users/signup.html")
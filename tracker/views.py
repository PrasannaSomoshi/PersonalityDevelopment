from django.shortcuts import render, HttpResponse, render, redirect
from .forms import UserForm, ChartForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Chart

# Create your views here.


def home(request):
    return render(request, 'index.html')


def register(request):
    form = UserForm

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(
                request, "Account created successfully for " + user)

            return redirect('/')

    context = {'form': form}
    return render(request, 'registration.html', context)


def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request, "Username or Password is incorrect")

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/login')


def dashboard(request):
    return render(request, 'dashboard.html')


def showTracker(request):
    form = ChartForm

    if request.method == "POST":
        form = ChartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/showReport')
        else:
            messages.info(request, "Could not enter details.Please try again")

    context = {'form': form}
    return render(request, 'trackerinput.html', context)


def showReport(request):
    report = Chart.objects.all()
    context = {'report': report}
    return render(request, 'report.html', context)

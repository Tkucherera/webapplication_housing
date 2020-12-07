from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.db.models import Q
from .filters import *
from django.views.generic import TemplateView, ListView
import os


def home(request):
    residences = Residence.objects.all
    return render(request, 'home.html', {'residences': residences})


def about(request):
    return render(request, 'About.html')


def athletes(request):
    return render(request, 'Athletes.html')


def contact(request):
    return render(request, 'contact_us.html')


def honors(request):
    return render(request, 'Honors_college.html')


def news(request):
    return render(request, 'News.html')


def issues(request):
    return render(request, 'Report_issue.html')


def residence(request):
    return render(request, 'Residences.html')


def apply(request):
    # this is supposed to filter the residences that a student can apply to
    def show_residences():
        userinfo = UserInfo.objects.all
        return userinfo


    # checking if the current user has information in the userinfo table
    info = 'False'
    if request.user.is_authenticated:
        current_user = str(request.user.get_username())
        for username in User.objects.all():
            if username.userinfo_set.all().exists():
                if str(username) == current_user:
                    info = 'J'
                    residences = Residence.objects.all
                    usersinfo = UserInfo.objects.all
                    return render(request, 'apply.html', {'residences': residences, 'info': info, 'userinfo': usersinfo})


    if request.method == 'POST':
        #user = request.user.username
        classification = request.POST['classification']
        sex = request.POST['sex']
        gpa = request.POST['gpa']
        sport = request.POST['sport']
        honors = request.POST['honors']
        age = request.POST['age']

        user = UserInfo(classification=classification, sex=sex, gpa=gpa, sport=sport, honors=honors, age=age, User=user)
        user.save()
        return redirect('apply')
    else:
        return render(request, 'apply.html', {'info': info})








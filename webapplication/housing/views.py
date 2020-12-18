from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.db.models import Q
from .filters import *
from django.contrib import messages


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


def pick_room(request):
    first = Q(floor__floor__contains=1)
    second = Q(floor__floor__contains=2)
    third = Q(floor__floor__contains=3)
    first_rooms = Rooms.objects.filter(first)
    second_rooms = Rooms.objects.filter(second)
    third_rooms = Rooms.objects.filter(third)
    results = {'first_rooms': first_rooms, 'second_rooms': second_rooms, 'third_rooms': third_rooms}

    return render(request, 'pickroom.html', results)


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
        username = request.user.get_username()
        classification = request.POST['classification']
        sex = request.POST['sex']
        gpa = request.POST['gpa']
        sport = request.POST['sport']
        honors = request.POST['honors']
        age = request.POST['age']

        user = UserInfo(classification=classification, sex=sex, gpa=gpa, sport=sport, honors=honors, age=age, username=username)
        user.save()
        return redirect('apply')
    else:
        return render(request, 'apply.html', {'info': info})


def thank_you(request):
    if request.method == 'POST':
        user = request.user.id
        reserve_room = request.POST['reserve']
        if User.objects.filter(id=user).exists():
            messages.info(request, 'Your Already have a Room Reserved')
            return render(request, 'thank_you.html')

        Rooms.objects.filter(id=reserve_room).update(Availability=False, occupant=user)
        return render(request, 'thank_you.html')





from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.db.models import Q
from .filters import *
from django.contrib import messages
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags



def home(request):
    residences = Residence.objects.all
    mySlides = MySlide.objects.all
    return render(request, 'home.html', {'residences': residences, 'mySlides': mySlides})


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
    if request.method == 'POST':
        user_id = request.user.id
        fullname = request.user.get_full_name
        room = Rooms.objects.get(id=user_id)
        building = room.residence.name
        suit = room.suit_num
        letter = room.room_letter
        email = request.user.email
        service = request.POST['service']
        problem_text = request.POST['problem']

        #variables to be parsed in email template
        context = {'service': service, 'fullname': fullname, 'building': building, 'suit': suit, 'letter': letter, 'email': email, 'problem': problem_text}

        #parameters for send mail
        subject = 'Report problem to ', service
        html_message = render_to_string('email.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'tinashedeveloper@gmail.com'
        to = 'liwodo1448@hafutv.com' #the email for either MPI, RA or IT
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message, fail_silently=False)

        return render(request, 'thank_you.html')


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
    user = request.user
    user_id = user.id
    if request.user.is_authenticated:
        if UserInfo.objects.filter(user=user_id).exists():
            info = 'J'
            residences = Residence.objects.all
            #get thr infomation of currently logged in user
            return render(request, 'apply.html', {'residences': residences, 'info': info})

    #when user inputs data for userinfor table
    if request.method == 'POST':
        classification = request.POST['classification']
        sex = request.POST['sex']
        gpa = request.POST['gpa']
        sport = request.POST['sport']
        honors = request.POST['honors']
        age = request.POST['age']

        user = UserInfo(classification=classification, sex=sex, gpa=gpa, sport=sport, honors=honors, age=age, user_id=user_id)
        user.save()
        return redirect('apply')
    else:
        return render(request, 'apply.html', {'info': info})


def thank_you(request):
    if request.method == 'POST':
        user = request.user.id
        reserve_room = request.POST['reserve']
        #checking if user has room already reserved
        if Rooms.objects.filter(occupant=user).exists():
            messages.info(request, 'Your Already have a Room Reserved')
            return render(request, 'thank_you.html')

        Rooms.objects.filter(id=reserve_room).update(Availability=False, occupant=user)
        return render(request, 'thank_you.html')





from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags



def register(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        #studentid = request.POST['student-id']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email taken')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            context = {'first_name': first_name}

            # parameters for send mail
            subject = 'Account Created'
            html_message = render_to_string('register_email.html', context)
            plain_message = strip_tags(html_message)
            from_email = 'tinashedeveloper@gmail.com'
            to = email  # the email for ne user
            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message, fail_silently=False)

            return redirect('home')
    else:
        return render(request, 'register.html', {'school': 'Falcon Nation'})


def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('apply')

        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')


def logout(request):
    auth.logout(request)
    return redirect('apply')


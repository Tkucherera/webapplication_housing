
from django.shortcuts import render
from django.db.models import Q
from django.apps import apps

rooms = apps.get_model('housing', 'Rooms')

def searchroom(request):
    if request.method == 'GET':
        query_residence = str(request.GET.get('residence'))
        query_suite = request.GET.get('suit_num')
        query_room_letter = request.GET.get('room_letter')
        residence = apps.get_model('housing', 'Residence')

        submitbutton = request.GET.get('submit')

        if query_suite is not None:
            lookups = Q(suit_num__icontains=query_suite)
            results = rooms.objects.filter(lookups).distinct()
            context = {'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'searchroom.html', context)

        else:
            return render(request, 'searchroom.html')

    else:
        return render(request, 'searchroom.html')


def reserveroom(request):
    if request.method == 'POST':
        room_taken=rooms.objects.filter(availability=request.availability).update(level=False)
        room_taken.save()
        return render(request, 'searchroom.html')



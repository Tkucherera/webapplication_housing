
from django.shortcuts import render
from django.db.models import Q
from django.apps import apps


def searchroom(request):
    if request.method == 'GET':
        query_residence = str(request.GET.get('residence'))
        query_suite = request.GET.get('suit_num')
        query_room_letter = request.GET.get('room_letter')
        rooms = apps.get_model('housing', 'Rooms')
        residence = apps.get_model('housing', 'Residence')

        submitbutton = request.GET.get('submit')

        if query_suite is not None:
            lookups = Q(suit_num__icontains=query_suite) | Q(room_letter__icontains=query_room_letter)
            lookup = Q(name__icontains=query_residence)
            results = rooms.objects.filter(lookups).distinct()
            houses = residence.objects.filter(lookup)
            context = {'houses' :houses, 'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'searchroom.html', context)

        else:
            return render(request, 'searchroom.html')

    else:
        return render(request, 'searchroom.html')


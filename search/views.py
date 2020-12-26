
from django.shortcuts import render
from django.db.models import Q
from django.apps import apps


rooms = apps.get_model('housing', 'Rooms')

def searchroom(request):
    if request.method == 'POST':
        residence = int(request.POST['residence'])
        suite = request.POST['suit_num']



        if residence is not None:
            results = rooms.objects.filter(residence_id=residence, suit_num=suite)
            context = {'results': results}
            return render(request, 'searchroom.html', context)

        else:
            return render(request, 'searchroom.html')

    else:
        return render(request, 'searchroom.html')





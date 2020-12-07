from django.contrib.auth.models import User
import django_filters
from .models import *


class RoomFilter(django_filters.FilterSet):
    residence = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Rooms
        fields = ['residence', 'floor', 'suit_num',  'room_letter']


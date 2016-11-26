from rest_framework import viewsets
from django.shortcuts import render
from django.views.generic import DetailView

from main.models import Line


class LineDetailView(DetailView):
    model = Line



class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

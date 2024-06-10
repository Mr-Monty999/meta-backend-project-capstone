from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import MenuItemSerializer,BookingSerializer
from .models import Menu,Booking

# Create your views here.


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class  BookingViewSet(viewsets.ModelViewSet):
   queryset =  Booking.objects.all()
   serializer_class =  BookingSerializer


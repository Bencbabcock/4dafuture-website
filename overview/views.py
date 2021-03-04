from django.shortcuts import render
from .models import Announcement

# Create your views here.

def home(request):
    announcements = Announcement.objects.all()
    return render(request, 'overview/home.html', {'announcements': announcements})

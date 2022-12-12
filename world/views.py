from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Profile
from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
#from .models import Restaurants

longitude = -6.3831
latitude = 53.404639

user_location = Point(latitude,longitude, srid=4326)

# class Home(generic.ListView):
#     model = Restaurants
#     context_object_name = 'restaurants'
#     queryset = Restaurants.objects.annotate(distance=Distance('location',
#     user_location)
#     ).order_by('distance')[0:6]
#     print(queryset.values())
#     template_name = 'index.html'
#
# home = Home.as_view


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



@login_required
def update_database(request):
    my_location = request.POST.get("point", None)
    if not my_location:
        return JsonResponse({"message": f"No location found. {my_location}"}, status=400)
    try:
        my_coords = [float(coord) for coord in my_location.split(", ")]
        my_profile = Profile.objects.get(user = request.user)
        my_profile.last_location = Point(my_coords)
        my_profile.save()

        message = f"Updated {request.user.username} with {f'POINT({my_location})'}"

        return JsonResponse({"message": message}, status=200)
    except:
        return JsonResponse({"message": "No profile found."}, status=400)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from main.models import Athlete, Therapist, Workout, SensorReading

# index page
def index(request):
    context = {
            "foo" : "bar",
    }
    return render(request, 'main/index.html', context)

# login page
def login(request):
    context = {
        "foo" : "bar",
    }
    return render(request, 'main/login.html', context)

# overview all athletes page
class OverviewView(generic.ListView):
    template_name = 'main/overview.html'
    context_object_name = 'athlete_list'

    def get_queryset(self):
        """
        Return the list of athletes that are registered with the logged-in physiotherapist
        """
        return Athlete.objects.all()

# heatmap & info for one athlete
def athlete(request, pk):
    context = {
        "foo" : "bar",
    }
    return render(request, 'main/athlete.html', context)

# page to add a new athlete
def add_athlete(request, pk):
    context = {
        "foo" : "bar",
    }
    return render(request, 'main/add_athlete.html', context)

# instruct server to add new athlete
def post_athlete(request):
    context = {
        "foo" : "bar",
    }
    return render(request, 'main/add_athlete.html', context)


def view_graph(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    plotted_graph = workout.readings_from_file()
    #context = {'plotted_graph': plotted_graph}
    return HttpResponse(plotted_graph)
    #return render(request, 'main/view_graph.html', context)
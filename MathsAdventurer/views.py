from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

from .models import User, Competition, Milestone, Resource, Topic, Difficulty, Event

from datetime import date
CURR_YEAR = date.today().year
GRADES = range(1, 13)
def index(request):
    return render(request, "MathsAdventurer/index.html")

def test(request):
    return render(request, "MathsAdventurer/layout.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "MathsAdventurer/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "MathsAdventurer/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "MathsAdventurer/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "MathsAdventurer/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "MathsAdventurer/register.html")
    
def competitions(request):
    if (request.user.is_authenticated):
        #allow user to add comp to his/her watchlist
        return render(request, "MathsAdventurer/competitions.html", {
        "competitions": Competition.objects.all(),
        "watchlist" : request.user.watchlist.all(),
        "grades" : GRADES
    })
    return render(request, "MathsAdventurer/competitions.html", {
        "competitions": Competition.objects.all(),
        "grades" : GRADES
    })
    
def topics(request):
    return render(request, "MathsAdventurer/resource_topics.html",{
        "topics" : Topic.objects.all()
    })

def resources(request, topic_id):
    if (not 1<= topic_id <= 5):
        return render(request, "MathsAdventurer/error.html",{
            "message": "ERROR: invalid topic chosen"
        })
    topic = Topic.objects.get(pk = topic_id)
    return render(request, "MathsAdventurer/resources.html", {
        "resources" : Resource.objects.filter(topic=topic),
        "difficulties" : Difficulty.objects.all()
    })

@login_required
def profile(request):
    return render(request, "MathsAdventurer/profile.html", {
        "competitions" : request.user.watchlist.all(),
        "milestones" : request.user.user_milestones.filter(year__gte = CURR_YEAR)
    })
    
@csrf_exempt
@login_required
def status_update(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
    milestone = Milestone.objects.get(pk=data.get("milestone_id"))
    status = data.get("status")
    milestone.status = status
    milestone.save()
    return JsonResponse({"message": "Status updated successfully."}, status=201)

@csrf_exempt
@login_required
def watchlist_update(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
    comp = Competition.objects.get(pk=data.get("comp_id"))
    is_add = data.get("is_add")
    print(f"{comp} : {is_add}")
    if is_add:
        comp.users_watching.add(request.user)
    else:
        comp.users_watching.remove(request.user)
    comp.save()
    return JsonResponse({"message": "Watchlist updated successfully."}, status=201)

@csrf_exempt
@login_required
def new_milestone(request):
    if (request.method == 'POST'):
        comp_id = request.POST['competition']
        if (comp_id == '-1'):
            return render(request, "MathsAdventurer/error.html",{
                'message' : "ERROR: Please select the name of the maths competition."
            })
        competition = Competition.objects.get(pk = comp_id)
        year = int(request.POST['year'])
        round = int(request.POST['round'])
        placement = request.POST['placement'] 
        score = request.POST['score']
        placement = placement if placement else None
        score = score if score else None
        m = Milestone(user=request.user, competition=competition,year=year, round=round, placement=placement, score=score)
        m.save()
        return HttpResponseRedirect(reverse('profile'))

@login_required
def archive(request):
    return render(request, "MathsAdventurer/archive.html", {
        "milestones" : request.user.user_milestones.filter(year__lt = CURR_YEAR)
    })
    
def calendar(request):
    return render(request, "MathsAdventurer/calendar.html")

def get_events(request):
    if request.method != "GET":
        return JsonResponse({"error": "GET request required."}, status=400)
    events = Event.objects.all()
    competitions = Competition.objects.all()
    return JsonResponse({
        "message": "Events retrieved successfully.",
        "events" : serializers.serialize('json', events), 
        "competitions" : serializers.serialize('json', competitions)
                    }, status=201)
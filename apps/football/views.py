# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *

# Create your views here.
def index(request):
    context = {
        "users": User.objects.exclude(id=1)
    }
    return render(request, 'football/index.html', context)
def team(request):
    context = {
        "my_players": Player.objects.filter(owner = User.objects.get(id=2)),
        "my_starters": Player.objects.filter(owner = User.objects.get(id=2)).filter(status="drafted"),
        "my_rbs": Player.objects.filter(owner = User.objects.get(id=2)).filter(position = "running back"),
        "my_wrs": Player.objects.filter(owner = User.objects.get(id=2)).filter(position = "wide receiver"),
        "my_qbs": Player.objects.filter(owner = User.objects.get(id=2)).filter(position = "quarterback"),
        "my_tes": Player.objects.filter(owner = User.objects.get(id=2)).filter(position = "tight end"),

    }
    return render(request, 'football/team.html', context)
def players(request):
    context = {
        "players" : Player.objects.all(),
        "users" : User.objects.exclude(first_name="Gordon")
    }
    return render(request, 'football/players.html', context)
def teamx(request, user_id):
    print user_id
    context = {
        # switch context to be by id
        "user": User.objects.get(id=user_id),
        "my_players": Player.objects.filter(owner = User.objects.get(id=user_id)),
        "my_rbs": Player.objects.filter(owner = User.objects.get(id=user_id)).filter(position = "running back").exclude(play="started"),
        "my_wrs": Player.objects.filter(owner = User.objects.get(id=user_id)).filter(position = "wide receiver").exclude(play="started"),
        "my_qbs": Player.objects.filter(owner = User.objects.get(id=user_id)).filter(position = "quarterback").exclude(play="started"),
        "my_tes": Player.objects.filter(owner = User.objects.get(id=user_id)).filter(position = "tight end").exclude(play="started"),
        "drafted_rbs": Player.objects.filter(play="started").filter(owner = User.objects.get(id=user_id)).filter(position="running back"),
        "drafted_wrs": Player.objects.filter(play="started").filter(owner = User.objects.get(id=user_id)).filter(position="wide receiver"),
        "drafted_qbs": Player.objects.filter(play="started").filter(owner = User.objects.get(id=user_id)).filter(position="quarterback"),
        "drafted_tes": Player.objects.filter(play="started").filter(owner = User.objects.get(id=user_id)).filter(position="tight end"),
    }
    return render(request, 'football/teamx.html', context)

def editteam(request, user_id):
    print user_id
    
    the_user = User.objects.get(id=user_id)
    context = {
        "user": the_user,
    }
    return render(request, 'football/editteam.html', context)

def power(request):
    context = {
        "jay": "silent bob",
        "users": User.objects.exclude(last_name = "Freeman")
    }
    return render(request, 'football/power.html', context)

def updateteam(request, user_id):
    print "updating"
    print user_id
    if request.POST['authenticator']!= "codejoy":
        print "access denied"
        return redirect('/odell')
    x = User.objects.get(id=user_id)
    x.team_name = request.POST['team_name']
    x.first_name = request.POST['first_name']
    x.last_name = request.POST['last_name']
    x.wins = request.POST['wins']
    x.losses = request.POST['losses']
    x.power = request.POST['power']
    x.password = request.POST['password']
    x.email = request.POST['email']
    x.bio = request.POST['bio']
    x.save()
    
    # the coding dojo is missing a step in learning
    # they go straight into setting things to the post object, when we should first set things to sally
    return redirect('/team/'+ user_id)
    # redirect to that teams page
# update team

def qbs(request):
    context = {
        "qbs": Player.objects.filter(position = "quarterback"),
    }
    return render(request, 'football/qbs.html', context)
def rbs(request):
    context = {
        "rbs": Player.objects.filter(position = "running back"),
    }
    return render(request, 'football/rbs.html', context)
def wrs(request):
    context = {
        "wrs": Player.objects.filter(position = "wide receiver"),
    }
    return render(request, 'football/wrs.html', context)
def tes(request):
    context = {
        "tes": Player.objects.filter(position = "tight end"),
    }
    return render(request, 'football/tes.html', context)
def playerx(request, player_id):
    print player_id
    context = {
        "player": Player.objects.get(id=player_id),
    }
    return render(request, 'football/player.html', context)

def add(request):
    print "add"
    return render(request, 'football/add.html')

def create(request):
    print "create"
    print request.POST
    print request.POST['first_name']
    print request.POST['last_name']
    Player.objects.create(first_name = request.POST['first_name'], last_name=request.POST['last_name'], owner = User.objects.first(), position=request.POST['position'],nfl_team=request.POST['nfl_team'],rank=request.POST['rank'],summary=request.POST['summary'],identifier=request.POST['identifier'])
    print "working?"
    return redirect('/add')

def edit(request, player_id):
    print "editing"
    print player_id
    my_player = Player.objects.get(id=player_id)
    print my_player.position
    posish = my_player.position
    context = {
        "player": Player.objects.get(id=player_id),
        "posish": posish
    }
    return render(request, 'football/edit.html', context)

def update(request, player_id):
    if request.POST['password']!= "codejoy":
        print "access denied"
        return redirect('/odell')
    x = Player.objects.get(id=player_id)    
    if request.POST['owner'] == 'Maxwell':
        x.owner = User.objects.get(first_name="Maxwell")
        x.save()
    if request.POST['owner'] == 'Gordon':
        x.owner = User.objects.get(first_name="Gordon")
        x.save()
    if request.POST['owner'] == 'Chris':
        x.owner = User.objects.get(first_name="Chris")
        x.save()
    if request.POST['owner'] == 'Devon':
        x.owner = User.objects.get(first_name="Devon")
        x.save()
    if request.POST['owner'] == 'Devin':
        x.owner = User.objects.get(first_name="Devin")
        x.save()
    if request.POST['owner'] == 'Justin':
        x.owner = User.objects.get(first_name="Justin")
        x.save()
    if request.POST['owner'] == 'Trevor':
        x.owner = User.objects.get(first_name="Trevor")
        x.save()
    if request.POST['owner'] == 'Ernie':
        x.owner = User.objects.get(first_name="Ernie")
        x.save()
    if request.POST['owner'] == 'Andrew':
        x.owner = User.objects.get(first_name="Andrew")
        x.save()
    if request.POST['owner'] == 'Sven':
        x.owner = User.objects.get(first_name="Sven")
        x.save()
    if request.POST['owner'] == 'Michael':
        x.owner = User.objects.get(first_name="Michael")
        x.save()
    if request.POST['owner'] == 'Spencer':
        x.owner = User.objects.get(first_name="Spencer")
        x.save()
    if request.POST['owner'] == 'Dylan':
        x.owner = User.objects.get(first_name="Dylan")
        x.save()
    print "updating"
    print player_id
    print request.POST
    x.first_name = request.POST['first_name']
    x.last_name = request.POST['last_name']
    x.position = request.POST['position']
    if x.position == "running":
        print "BINGO runner"
        x.position = "running back"
    if x.position == "wide":
        print "BINGO RECEIVER"
        x.position = "wide receiver"
    if x.position == "tight":
        print "BINGO Tight end"
        x.position = "tight end"

    x.bye = request.POST['bye']
    x.nfl_team = request.POST['nfl_team']
    x.identifier = request.POST['identifier']

    x.summary = request.POST['summary']

    x.rank = request.POST['rank']
    x.touchdowns = request.POST['touchdowns']
    x.points = request.POST['points']
    x.save()
    # get player and then make a variable and make changes and save variable
    return redirect('/player/'+player_id)

def draft(request):
    print "drafting"
    context = {
        "players": Player.objects.all(),
        "undrafted": Player.objects.filter(status="undrafted"),
        "drafted": Player.objects.filter(status="drafted"),
    }
    return render(request, 'football/draft.html', context)

def drafting(request, player_id):
    print "drafting this player"
    print player_id
    x = Player.objects.get(id=player_id)
    x.status = "drafted"
    x.save()
    # get player and then make a variable and make changes and save variable
    return redirect('/draft')

def starting(request, user_id, player_id):
    print "starting this player"
    print player_id
    print "for this user"
    print user_id
    x = Player.objects.get(id=player_id)
    p = x.position
    print p
    u = User.objects.get(id=user_id)
    l = len(Player.objects.filter(position="quarterback").filter(owner = u).filter(play="started"))
    r = len(Player.objects.filter(position="running back").filter(owner = u).filter(play="started"))
    w = len(Player.objects.filter(position="wide receiver").filter(owner = u).filter(play="started"))
    t = len(Player.objects.filter(position="tight end").filter(owner = u).filter(play="started"))

    if l>0 and p == "quarterback":
        print "cannot add qb"
        print l
        return redirect('/team/' + user_id)
    if r>2 and p == "running back":
        print "cannot add rb"
        print r
        return redirect('/team/' + user_id)
    if w>2 and p == "wide receiver":
        print "cannot add wr"
        print w
        return redirect('/team/' + user_id)
    if t>1 and p == "tight end":
        print "cannot add te"
        print t
        return redirect('/team/' + user_id)
    x.status = "drafted"
    x.play = "started"
    x.save()
    # get player and then make a variable and make changes and save variable
    return redirect('/team/' + user_id)

def redraft(request, player_id):
    print "redrafting this player"
    print player_id
    x = Player.objects.get(id=player_id)
    x.status = "undrafted"
    x.save()
    # get player and then make a variable and make changes and save variable
    return redirect('/draft')

def sit(request, user_id, player_id):
    print "sitting this player"
    print player_id
    print "for this user"
    print user_id
    x = Player.objects.get(id=player_id)
    x.play = "benched"
    x.save()
    # get player and then make a variable and make changes and save variable
    return redirect('/team/' + user_id)

def odell(request):
    return render(request, 'football/odell.html')
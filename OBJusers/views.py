###############################################################################################################
# Views.py                                                                                                    #
# Author: Mayra Lanza                                                                                         #
###############################################################################################################
# Objective Gaming                                                                                            #
# Esports page                                                                                                #
# Gioker - Admin User : can add events, and create teams on the page 1-*. Be able to add images to the logo   #
#       >> Each event page will display team + members                                                        #
#       >> Members are able to join a team/or follow the event                                                #
# Feed Page - Events. If store clicked, the page will show details of the members and what is the event about #
# Urls:                                                                                                       #
#       /Home - Index/Feed - see all events - login required                                                  #
#       /Teams - details of the teams - available to everyone                                                 #
#       /Profile - User Profile - User can join teams, and follow events - Only available to user             #
#                   >> the feed by default will show the events of the team, and the followed ones            #
#                - User can add events  - login required                                                      #
###############################################################################################################
from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Event, Team, TeamMember, Profile
from django.views import View
from django.contrib.auth import logout
import requests

# Log out function
class LogoutView(View):
    template_name = 'registration/logged_out.html'
    def get(self, request):
        response = logout(request)

        return render(response, self.template_name)

# Home page will display all the events created by the users, and Merch (no enabled)
@login_required(login_url="/login")
def home(request):
    # User can follow and unfollow any event
    following = request.user.events.all() 
    events = Event.objects.all()
    # The Follow/Unfollow button has been pressed
    if request.method == "POST":
        event_id = request.POST.get("event-id")
        follow_id = request.POST.get("follow-id")
        unfollow_id = request.POST.get("unfollow-id")
        print('follow_id:' + str(follow_id))
        print('unfollow_id:' + str(unfollow_id))
        current_user = request.user
        # Delete: Author of the event may delete the event
        if event_id:
            event_del = Event.objects.filter(id=event_id).first()
            if event_del and (event_del.author == request.user ):
                event_del.delete()
        # Follow 
        if follow_id:
            event_foll = Event.objects.filter(id=follow_id).first()
            print(event_foll)
            event_foll.user.add(current_user)
        # Unfollow
        if unfollow_id:
            event_unfoll = Event.objects.get(id=unfollow_id)
            currentUserObj = User.objects.get(username=current_user)
            print(event_unfoll)
            print(currentUserObj)
            event_unfoll.user.remove(currentUserObj)
    return render(request, 'OBJusers/home.html', {"events": events,'following':following})

# the teams page will diaplay all the teams formed in the organization
# Members of a team will display custom image when using keywords
# League of Legends roles: Support, ADC, Jungle, Mid, Top
# Apex roles: Support, Fragger, Recon
# Valorant roles: Initiator, Controller
# There is a default OBJ image when the above is misppelled or if there is a custom role
def team(request):
    teams = TeamMember.objects.all()
    matches_array = {}
    # This part was for the website to get players' stats. Is not displayed in the website yet.
    # for member in teams: 
    #     if str(member.team)== "League of Legends":
    #         riot_id=member.game_id
    #         api_key = "RGAPI-8814b6a0-6a79-43b4-a51e-6f4c633ba616"
    #         api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"+ riot_id +"/ids?start=0&count=3"
    #         api_url= api_url + "&api_key=" + api_key
    #         resp =  requests.get(api_url)
    #         matches = resp.json()
    #         matches_array[member.member]= matches
    #         #Getting one match data
    #         match = matches_array[member.member][0]
    #         api_match_url = "https://americas.api.riotgames.com/lol/match/v5/matches/"+match
    #         api_match_url = api_match_url + "?api_key=" + api_key
    #         match_resp = requests.get(api_match_url) 
    #         game = match_resp.json()
    #         player_index = game["metadata"]["participants"].index(riot_id)
    #         game_info = []
    #         game_info.append(game["info"]["participants"][player_index]["championName"])
    #         game_info.append(game["info"]["participants"][player_index]["kills"])
    #         game_info.append(game["info"]["participants"][player_index]["deaths"])
    #         game_info.append(game["info"]["participants"][player_index]["assists"])
    #         game_info.append(game["info"]["participants"][player_index]["goldEarned"])
    #         print(game_info)
    game_info = []
    return render(request, 'OBJusers/teams.html', {"teams": teams, "League_matches": matches_array, "game_info":game_info})

# In the profile page, the user can add events. Moreover, they can see how many events they have followed
@login_required(login_url="/login")
def profile(request):
    current_user = request.user
    teams = TeamMember.objects.filter(member=current_user)
    choice_teams = Team.objects.all()
    events_followed_count = Event.objects.filter(user=current_user).count()
    # Create Event
    if request.method == 'POST':
            event = Event()
            event.event = request.POST['event']
            team_id = request.POST['useroption']
            team_sel = Team.objects.get(id=team_id)
            event.team = team_sel
            event.author = request.user
            event.description = request.POST['desc']
            for key,value in request.FILES.items():
                print(key)
                print(value)
                event.file = value
            event.save()
            return render(request, 'OBJusers/profile.html',  {"teams": teams, "choice_teams": choice_teams, 'events_followed_count': events_followed_count})
    return render(request, 'OBJusers/profile.html',  {"teams": teams, "choice_teams": choice_teams, 'events_followed_count': events_followed_count})

@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()

    return render(request, 'OBJusers/create_post.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

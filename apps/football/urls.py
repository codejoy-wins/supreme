from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^team$', views.team),
    url(r'^players$', views.players),
    url(r'^team/(?P<user_id>\d+)$', views.teamx),
    url(r'^edit/team/(?P<user_id>\d+)$', views.editteam),
    url(r'^update/team/(?P<user_id>\d+)$', views.updateteam),
    url(r'^power$', views.power),
    url(r'^qbs$', views.qbs),
    url(r'^rbs$', views.rbs),
    url(r'^wrs$', views.wrs),
    url(r'^tes$', views.tes),
    url(r'^player/(?P<player_id>\d+)$', views.playerx),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^edit/(?P<player_id>\d+)$', views.edit),
    url(r'^update/(?P<player_id>\d+)$', views.update),
    url(r'^draft$', views.draft),
    url(r'^drafting/(?P<player_id>\d+)$', views.drafting),
    url(r'^redraft/(?P<player_id>\d+)$', views.redraft),
    url(r'^starting/(?P<user_id>\d+)/(?P<player_id>\d+)$', views.starting),
    url(r'^sit/(?P<user_id>\d+)/(?P<player_id>\d+)$', views.sit),

    url(r'^', views.odell),
]
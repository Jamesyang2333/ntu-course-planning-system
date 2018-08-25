
from django.conf.urls import url
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^timetable/search/$', views.search,name='search'),
    url(r'^home/$',views.mainpage,name='home'),
    url(r'^timetable/$',views.timetable,name='timetable'),
    url(r'^contact/$',views.contact,name='contact'),
    #url(r'^forum/$',views.forum,name='forum'),
url(r'^forum/$',views.temp,name='temp'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^forum/(?P<myindex_name_url>\w+)/$', views.myindex, name='myindex'),
    url(r'^forum/(?P<coursecode1_name_url>\w+)/$', views.coursecode, name='coursecode'),
    url(r'^add_myindex/$', views.add_myindex, name='add_myindex'),
    url(r'^contact/success/$',views.successView,name='success'),


    #url(r'^forum/(?P<myindex_name_url>\w+)/add_expectedindex/$', views.add_expectedindex, name='add_expectedindex'),
    #url(r'^/forum/(?P<myindex_name_url>\w+)/(?P<expectedindex_name_url>\w+)/$', views.expectedindex, name='expectedindex'),
]
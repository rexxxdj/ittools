from django.conf.urls import include, url
from team import views

urlpatterns = (
    #url(r'^$', views.main_page,name='home'),
    url(r'^$',views.team_list,name='team'),
)
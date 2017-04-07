from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from team import views


urlpatterns = [
    #url(r'^$', views.main_page,name='home'),
    url(r'^$',views.team_list,name='team'),
    url(r'^(?P<uid>\d+)/$',views.team_unit,name='team_unit'),
    url(r'^add/$',views.worker_add,name='worker_add'),
    #url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
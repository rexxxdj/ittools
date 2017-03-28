from django.conf.urls import include, url
from services import views

urlpatterns = (
    url(r'^$',views.service_list,name='service'),
    url(r'^(?P<sid>\d+)/$',views.service_unit,name='service unit'),
)
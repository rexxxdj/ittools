from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from services import views

urlpatterns = [
    url(r'^$',views.service_list,name='service'),
    url(r'^(?P<sid>\d+)/$',views.service_unit,name='service unit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from services.views import services
from services.views import journal

urlpatterns = [
    url(r'^$',services.service_list,name='service'),
    url(r'^(?P<sid>\d+)/$',services.service_unit,name='service unit'),
    url(r'^journal/$',journal.JournalView.as_view(),name='journal')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
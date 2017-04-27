#from django.contrib.auth import views as auth_views
#from django.views.generic.base import RedirectView
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from services.views import services
from services.views import journal

urlpatterns = [
    url(r'^$',services.service_list,name='service'),
    url(r'^journal/$',journal.JournalView.as_view(),name='journal'), 
    # registration/autorisation urls
    #url(r'^users/logout/$', auth_views.logout, kwargs={'next_page':'index'}, name='auth_logout'),
    #url(r'^register/complete/$', RedirectView.as_view(pattern_name='index'), name='registration_complete'),
    #url(r'^users/', include('registration.backends.simple.urls', namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""ittools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView, RedirectView
from services.views import services
import views
from team import urls as team_urls
from services import urls as service_urls

urlpatterns = (
    #index urls
    url(r'^$',views.index_list,name='index'),
    #services urls
    url(r'^services/', include(service_urls)),
    #team urls
    url(r'^team/', include(team_urls)),
    # app urls           
    url(r'^admin/', include(admin.site.urls)),
    # registration/autorisation urls
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page':'index'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='index'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),
)

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from exuser.views import login
# to use django's authentcating system add below lines
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    # url(r'^$', login, name='login'),
    # to use django's authentcating system add below lines
    url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'} ,name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'core/logged_out.html'},name='logout'),
]

# For static files url
if settings.DEBUG is True:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# for uploads 
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
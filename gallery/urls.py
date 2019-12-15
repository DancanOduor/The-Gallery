from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin
# from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView


urlpatterns=[
    url('^$',views.image,name = 'image'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^detail/(\d+)', views.detail, name='detail'),
    url(r'^location/(\d+)', views.location, name='location'),
    url(r'^share/(\d+)', views.share, name='share'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    # url('', views.homepageview, name='home'),
]
## new static route that references the location to the uploaded files
if settings.DEBUG: 
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# Serving the media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
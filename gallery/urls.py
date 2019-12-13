from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[
    url('^$',views.image,name = 'image'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^detail/(\d+)', views.detail, name='detail'),
    url(r'^location/(\d+)', views.location, name='location'),
    url(r'^share/(\d+)', views.share, name='share'),
]
## new static route that references the location to the uploaded files
if settings.DEBUG: 
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
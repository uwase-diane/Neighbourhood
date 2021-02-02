from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^new/profile$', views.add_profile, name='edit'),
    url(r'^myprofile$',views.my_profile,name ='myprofile'),
    url('^addhood',views.addhood,name='addhood'),
    url(r'^detail/(?P<neighbourhood_id>\d+)/$',views.neighbourhood_details, name='detail'),
    url(r'^new_business/(?P<pk>\d+)/$' , views.new_business,name='new_business'),
    url(r'^new_post/(?P<pk>\d+)$', views.new_post,name='new_post'),
    url(r'^search/$', views.search_project, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
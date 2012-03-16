from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'provisioning.base.views.index'),
    (r'^snom/', include('provisioning.snom.urls')),
    (r'^gxp/', include('provisioning.grandstream.urls')),
)
urlpatterns += staticfiles_urlpatterns()

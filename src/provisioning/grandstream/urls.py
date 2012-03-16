from django.conf.urls.defaults import patterns, include, url

"""
no documentation yet
"""

urlpatterns = patterns('provisioning.grandstream.views',
    # info page
    url(r'^$', 'index'),
)

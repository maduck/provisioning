from django.conf.urls.defaults import patterns, include, url

"""
http://downloads.snom.net/documentation/md_rev2.pdf

/snom3x0.htm
-> /3x0/general.xml
   -> /3x0/firmware.xml

/3x0/phone.xml
/3x0/fkeys.xml
/3x0/tbook.xml
/3x0/dplan.xml

/3x0/mac/phone.xml
/3x0/mac/fkeys.xml
/3x0/mac/tbook.xml
/3x0/mac/dplan.xml

/snom3x0-mac.htm
-> /3x0/mac.xml
"""

urlpatterns = patterns('provisioning.snom.views',
    url(r'^$', 'index'),
    url(r'^snom(?P<version>\d+)-firmware.htm', 'firmware_info'),

    url(r'^snom(?P<version>\d+).htm$', 'general_info'),
    url(r'^snom(?P<version>\d+)-(?P<mac_address>.+).htm$', 'specific_info'),
    url(r'^(?P<version>\d+)/(?P<config>.+).xml', 'general_xml'),
    url(r'^(?P<version>\d+)/(?P<mac_address>.+)/(?P<config>.+).xml', 'specific_xml'),
)

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
    # info page
    url(r'^$', 'index'),
    # firmware upgrade
    url(r'^snom(?P<version>\d+)-firmware.htm', 'firmware_info'),

    # general and specific phone settings
    url(r'^(?P<version>\d+)/(?P<config>\D+).xml', 'xml_settings'),
    url(r'^(?P<version>\d+)/(?P<config>\D+)-(?P<mac_address>.+).xml', 'xml_settings'),

    # unused by now.
    url(r'^snom(?P<version>\d+).htm$', 'general_info'),
    url(r'^snom(?P<version>\d+)-(?P<mac_address>.+).htm$', 'specific_info'),
)

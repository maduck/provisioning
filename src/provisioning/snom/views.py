from django.shortcuts import render_to_response
from django.http import Http404

def index(request):
    return render_to_response('snom/index.html', {})

def xml_settings(request, version, config, mac_address=None):
    if mac_address is not None:
        return render_to_response('snom/config/settings-%s.xml' % mac_address)
    return render_to_response('snom/config/settings.xml')

def general_info(request, version):
    return render_to_response('snom/index.html', {})

def firmware_info(request, version):
    raise Http404('sorry. implementing this later.')
    return render_to_response('snom/index.html', {})

def specific_info(request, version, mac_address):
    return render_to_response('snom/index.html', {'mac': mac_address})

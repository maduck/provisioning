from django.shortcuts import render_to_response

def index(request):
    return render_to_response('snom/index.html', {})

def general_info(request, version):
    return render_to_response('snom/index.html', {})

def firmware_info(request, version):
    return render_to_response('snom/index.html', {})

def specific_info(request, version, mac_address):
    return render_to_response('snom/index.html', {'mac': mac_address})

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext

import json

from scripts.django_cam_controller import capture_image, get_pid, capture_interval


def home(request):
    context_instance = RequestContext(request)

    context = {'request': request, }

    return render_to_response("home.html", context, context_instance=context_instance)


def take_image(request):
    
    capture_image()

    data = {
        "success": "image captured"
    }

    return HttpResponse(json.dumps(data), content_type="application/json")

def clear_mount(request):
    get_pid()
    
    data = {
        "success": "camera unmounted"
    }
    
    return HttpResponse(json.dumps(data), content_type="application/json")

def take_interval(request):
    sec = request.GET["sec"]
    capture_interval(sec)

    data = {
        "success": "Capturing at interval"
    }

    return HttpResponse(json.dumps(data), content_type="application/json")
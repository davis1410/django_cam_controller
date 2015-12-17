from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext

import json

from scripts.django_cam_controller import capture_image, get_pid


def take_image(request):
    image_dir = request.GET['image_dir']
    print image_dir
    
    capture = capture_image(image_dir)

    data = {
        "success": capture
    }

    return HttpResponse(json.dumps(data), content_type="application/json")

def clear_mount(request):
    clear_mount = get_pid()
    
    data = {
        "success": clear_mount
    }
    
    return HttpResponse(json.dumps(data), content_type="application/json")

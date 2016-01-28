from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext

import json

from scripts.django_cam_controller import *


def take_image(request):
    capture = capture_image()

    data = {
        "result": capture
    }

    return HttpResponse(json.dumps(data), content_type="application/json")


def take_interval(request):
    frames = request.GET["frames"]
    sec = request.GET["sec"]
    capture = capture_interval(frames, sec)

    data = {
        "result": capture
    }

    return HttpResponse(json.dumps(data), content_type="application/json")


def compile_preview(request):
    framerate = request.GET['framerate']
    
    compile = compile_video(framerate)
    
    data = {
        "result": compile
    }
    
    return HttpResponse(json.dumps(data), content_type="application/json")

def new_sequence_creation(request):
    sequence = new_sequence()
    
    data = {
        "result": sequence
    }
    
    return HttpResponse(json.dumps(data), content_type="application/json")
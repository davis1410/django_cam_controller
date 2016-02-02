from django.conf.urls import *

urlpatterns = [
    url(r'^take_image/$', 'django_cam_controller.views.take_image'),
    url(r'^get_num_images/$', 'django_cam_controller.views.get_num_images'),
    url(r'^clear_mount/$', 'django_cam_controller.views.clear_mount'),
    url(r'^take_interval/$', 'django_cam_controller.views.take_interval'),
    url(r'^compile_preview/$', 'django_cam_controller.views.compile_preview'),
    url(r'^new_sequence_creation/$', 'django_cam_controller.views.new_sequence_creation')
]

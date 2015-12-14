from django.conf.urls import *

urlpatterns = [
    url(r'^$', 'django_cam_controller.views.home'),
    url(r'^take_image/$', 'django_cam_controller.views.take_image'),
    url(r'^clear_mount/$', 'django_cam_controller.views.clear_mount')
]

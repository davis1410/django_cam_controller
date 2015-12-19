import os, re, subprocess

user_dir = os.path.expanduser('~')

def capture_image():
    capture_image = subprocess.Popen(['gphoto2', '--capture-image-and-download', '--filename', 'django_cam_controller/static/img/%:', '--keep'], stdout=subprocess.PIPE)
    capture_result = capture_image.stdout.read()

    os.system("gphoto2 --summary")

    return capture_result

def capture_interval(frames ,sec):
    if (sec):
        os.system("gphoto2 --capture-image -F %s --interval %s" % (frames, sec))
        
        message = "Capturing at interval of %s for %s frames." % (sec, frames)
        
    else:
        message = "No interval set. Please set an interval (in seconds)."

    return message

def compile_video(framerate):
    os.chdir('django_cam_controller/static/img/')
    os.system("mogrify -auto-orient -resize 800x600! *.jpg")
    
    os.system("ffmpeg -y -pattern_type glob -framerate %s -i '*.jpg' -an -s hd720 -vcodec libx264 -pix_fmt yuv420p -preset slow -profile:v baseline -movflags faststart ../video/preview.mp4" % framerate)
    
    os.chdir("../../../")
    
    message = "Movie compiled"
    
    return message


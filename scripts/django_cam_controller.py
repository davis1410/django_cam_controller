import os, re, subprocess

user_dir = os.path.expanduser('~')

def num_images():
    n1 = subprocess.Popen(['ls', 'django_cam_controller/static/img'], stdout=subprocess.PIPE)
    n2 = subprocess.Popen(['wc', '-l'], stdin=n1.stdout, stdout=subprocess.PIPE)
    result = n2.stdout.read()
    
    num_images = result.replace("\n", "")
    
    return num_images

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

def new_sequence():
    img_dir = "django_cam_controller/static/img"
    os.system("rm -rf %s" % img_dir)
    os.makedirs(img_dir)
    
    message = "Ready to capture new sequence"
    
    return message
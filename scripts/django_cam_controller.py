import os, re, subprocess

user_dir = os.path.expanduser('~')

def capture_image():
    #os.system("gphoto2 --set-config capturetarget=1 --capture-image")
    capture_image = subprocess.Popen(['gphoto2', '--set-config', 'capturetarget=1', '--capture-image'], stdout=subprocess.PIPE)
    capture_result = capture_image.stdout.read()

    os.system("gphoto2 --summary")

    return capture_result
    
def get_pid():
    p1 = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', '-i', 'gphoto'], stdin=p1.stdout, stdout=subprocess.PIPE)
    process = p2.stdout.read()
    print process
    
    pid = re.search( '\npi\s+(\d+).+gphoto2 --spawner.+', process, re.M )

    message = ''

    if pid:
        os.system('kill -9 %s' % pid.group(1))
        os.system('ps aux | grep -i "gphoto"')
        message = "Camera unmounted and ready to use."
    else:
        message = "Nothing to unmount."

    return message

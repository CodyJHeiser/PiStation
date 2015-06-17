import os, time

def findfiles(filename):
    base = "/home/pi"
    target = filename
    global PiPath
    for root, dirs, files in os.walk(base):
        if target in files:
            time.sleep(0.3)
            print "File Found!"
            PiPath = os.path.join(root, target)
            return

findfiles(PiFM2.py)

print "Press any key to install PiFM to the /home/pi directory"
raw_input()

os.system("cd /home/pi")

os.system("wget http://omattos.com/pifm.tar.gz")
os.system("tar -xvf pifm.tar.gz")
os.system("rm pifm.tar.gz")
os.system("apt-get install ffmpeg")

print "All done, press enter to quit or 'P' to open PiStation"

choice = raw_input("\n").lower()

if choice == " ":
    os.system("sudo python ./PiFM2.py")
elif choice == "":
    exit()

import os, time
current_dir = os.system("pwd") #Shows current directory

def loading(): #Loading for show (you can comment out if you want to)
    print "loading"
    clear(.3,0)
    print "loading."
    clear(.3,0)
    print "loading.."
    clear(.3,0)
    print "loading..."
    clear(.3,0)
    print "loading"
    clear(.3,0)
    print "loading."
    clear(.3,0)
    print "loading.."
    clear(.3,0)
    print "loading..."
    clear(.3,0)


def findpifm():
    base = "/home/pi"
    target = "pifm"
    global pifm_path
    for root, dirs, files in os.walk(base):
        if target in files:
            time.sleep(0.3)
            pifm_path = os.path.join(root, target)
            return


def movepifm(): #If PiFM is in a different directory, it copies it to the 'pi' folder
    if pifm_path == "/home/pi":
        exit()
    else:
        os.system("cp " + pifm_path + " /home/pi")

def changedir(): #Changes directory to /home/pi if you're not there already
    if current_dir == "/home/pi":
        exit()
    else:
        os.system("cd /home/pi")

findpifm()
movepifm()


class bcolors: #colors used in findfiles (below)
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def findfiles(filename):
    base = "/home/pi"
    target = filename
    global SongPath
    for root, dirs, files in os.walk(base):
        if target in files:
            time.sleep(0.3)
            print "File Found!"
            SongPath = os.path.join(root, target)
            return
        else:
            SongPath = "Sorry the file, " + bcolors.WARNING + SongName + bcolors.ENDC + " doesn\'t seem to exist" #holding a value (required)
            #You can un-commnet 'SongPath' here (below), but it repeats a coulple of times when searching
            #print SongPath
            SongPath = "0"


def clear(t1, t2):
    time.sleep(t1)
    os.system("clear")
    time.sleep(t2)


def find_type(Song_Path):
    global Song_type
    if ".mp3" in Song_Path.lower():
        Song_type = "001"
    elif ".wav" in Song_Path.lower():
        Song_type = "002"
    else:
        Song_type = "003"
        print "Sorry that file extension isn\'t supported!"
        exit()


def Station_Selector():
    print "Please enter your Frequency, anywhere between 87.1 and 108.2"
    freq = float(raw_input())
    if freq <=  87.1 :
        print "\nPlease keep the frequency above 87.1"
        quit()
    elif freq >= 108.2 :
        print "\nPlease keep the frequency below 108.1"
        quit()
    else:
        loading()
        if Song_type == "001": #MP3 File
            os.system("ffmpeg -i " + SongPath + " -f s16le -ar 22.05k -ac 1 - | sudo ./pifm - " + str(freq))
        elif Song_type == "002": #WAV FILE
            os.system("sudo ./pifm " + SongPath + " " + str(freq) + " 22050 stereo")
        elif Song_type == "003":
            print "There was a strange error!  Please re-download the program and try again!  \nIf the problem persist, contact me at CodyJHeiser@gmail.com"
            clear(1.4,0)
            raw_input("press any key to continue")
            exit()
        else:
            print"There was a strange error!  Please re-download the program and try again!  \nIf the problem persist, contact me at CodyJHeiser@gmail.com"
            clear(1.4,0)
            raw_input("press any key to continue")
            exit()
        
def main():
    clear(0,0)
    print ("Welcome to PiFM!  \nVersion 2.1 \nGPLv3 License")
    clear(1.3,0)
    print ("Enter the file you would like to play here! \nWatch Capitalization!")
    global SongName
    SongName = raw_input("\n")
    time.sleep(0.3)
    findfiles(SongName)
    if SongPath == "0":
        clear(.4,.8)
        print "Sorry, couldn\'t find your file!  Please try again!"
        exit()
    clear(0.8,0)
    find_type(SongPath)
    Station_Selector()
    
main()

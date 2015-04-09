#!/bin/python

import os, argparse
current_dir = os.system("pwd") #Shows current directory

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
            print "File Found!"
            SongPath = os.path.join(root, target)
            return
        else:
            SongPath = "Sorry the file, " + WARNING + SongName + ENDC + " doesn\'t seem to exist" #holding a value (required)
            #You can un-commnet 'SongPath' here (below), but it repeats a coulple of times when searching
            #print SongPath
            SongPath = "0"

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
    freq = None
    while 87.1 >= freq >= 108.2:
        print "Please enter your Frequency, anywhere between 87.1 and 108.2"
        freq = float(raw_input("> "))
    try:
        loading()
        if Song_type == "001": #MP3 File
            os.system("ffmpeg -i " + SongPath + " -f s16le -ar 22.05k -ac 1 - | sudo ./pifm - " + str(freq))
        elif Song_type == "002": #WAV FILE
            os.system("sudo ./pifm " + SongPath + " " + str(freq) + " 22050 stereo")
    except Exception:
        print "There was an exception. Halting."
        exit()

parser = argparse.ArgumentParser(prog='python PiStation.py', description='Broadcasts WAV/MP3 file over FM using RPI GPIO #4 pin.')


def main():
    os.system('clear')
    print ("Welcome to ImPiFM!  \nVersion 1.0 \nGPLv3 License")
    os.system('clear')
    print ("Enter the file you would like to play here! \nWatch Capitalization!")
    global SongName
    SongName = raw_input("\n")

    findfiles(SongName)
    if SongPath == "0":
        os.system('clear')
        print "Sorry, couldn\'t find your file!  Please try again!"
        exit()
    os.system('clear')
    find_type(SongPath)
    Station_Selector()
    
if __name__ == '__main__':
    main()

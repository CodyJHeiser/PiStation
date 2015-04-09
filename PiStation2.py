#!/usr/bin/python

import os, argparse

parser = argparse.ArgumentParser(prog='python PiStation.py', description='Broadcasts WAV/MP3 file over FM using RPI GPIO #4 pin.')
parser.add_argument("song_file")
parser.add_argument("-f", "--frequency", help="Set TX frequency. Acceptable range 87.1-108.2", type=float)
arg = parser.parse_args()

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def Station_Selector():
    if arg.frequency 87.1 <= freq <= 108.2: freq = arg.frequency
    else:
        print "Frequency argument out of range."
        freq = 0
        while 87.1 <= freq <= 108.2:
            print "Please enter your Frequency, anywhere between 87.1 and 108.2"
            freq = float(raw_input("> "))
    try:
        if ".mp3" in args.song_file.lower():
            os.system("ffmpeg -i " + SongPath + " -f s16le -ar 22.05k -ac 1 - | sudo ./pifm - " + str(freq))
        elif ".wav" in args.song_file.lower():
            os.system("sudo ./pifm " + SongPath + " " + str(freq) + " 22050 stereo")
        else:
            print "Sorry that file extension isn't supported or the file does not exist!"
            print "File name provided: %s" %(WARNING + SongName + ENDC)
            exit()
    except Exception:
        print "There was an exception. Halting."
        exit()



def main():
    #os.system('clear')
    print ("Welcome to ImPiFM!  \nVersion 1.0 \nGPLv3 License")
    #os.system('clear')
    Station_Selector()
    
if __name__ == '__main__':
    main()

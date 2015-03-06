import os, time
error256 = "\nMake sure that your file ends in either all caps or all lowercase.\nEX. Somesong.WAV or Somesong.wav not Somesong.WaV."
reboot = "\nWe will now attempt to restart the program"
rebootask = "\nWould you like us to attempt to reboot the program?"
error404 = "Keep getting this error?  When it asks you to press enter type 'continue' without the quotes to bypass this"
error1 = "Looks like you don't have 'ffmpeg' isntalled, we will install it for you, it that okay?"
error2 = "We were unable to detect your system information, would you like to attempt to continue anyway?"
os.system("clear")

def ftwav():
        os.system("clear")
        print "Does the song sound to fast, slow, or just not playing at all? Check the README files."
        check1 = os.system("sudo ./pifm " + direct + " " + str(freq) + " 22050 stereo")
        rebootpro()

def ftmp3():
        os.system("clear")
        print "Does the song sound to fast, slow, or just not playing at all? Check the README files."
        os.system("ffmpeg -i " + direct + " -f s16le -ar 22.05k -ac 1 - | sudo ./pifm - " + str(freq))
        rebootpro()

def countdownspec():
            print "Are you sure you want to go into BYPASS mode?  Some features may not work while in it"
            bypassmode = raw_input("\nY/N\n").lower()
            if bypassmode == "y":
                os.system("clear")
                print "starting BYPASS MODE in 5"
                time.sleep(1)
                os.system("clear")
                print "starting BYPASS MODE in 4"
                time.sleep(1)
                os.system("clear")
                print "starting BYPASS MODE in 3"
                time.sleep(1)
                os.system("clear")
                print "starting BYPASS MODE in 2"
                time.sleep(1)
                os.system("clear")
                print "starting BYPASS MODE in 1"
                time.sleep(2)
            else:
                quit()

def countdown():
        error1answ = raw_input("Y/N\n").lower() #.lower() turnes your answer into all lower case
        if error1answ == "y":
            time.sleep(1)
            print "Please press 'Y' if it asks you"
            time.sleep(2)
            os.system("sudo apt-get install ffmpeg")
            print reboot
            time.sleep(2)
            os.system("clear")
            print error404
            time.sleep(4)
            os.system("clear")
            print "Your may have to manually restart"
            print "restarting in 5"
            time.sleep(1)
            os.system("clear")
            print "Your may have to manually restart"
            print "restarting in 4"
            time.sleep(1)
            os.system("clear")
            print "Your may have to manually restart"
            print "restarting in 3"
            time.sleep(1)
            os.system("clear")
            print "Your may have to manually restart"
            print "restarting in 2"
            time.sleep(1)
            os.system("clear")
            print "Your may have to manually restart"
            print "restarting in 1"
            time.sleep(1)
            os.system("python pistation.py")
        else:
            quit()

def rebootpro():
        print rebootask
        ask1 = raw_input("Y/N\n").lower()
        if ask1 == "y":
            os.system("python pistation.py")
        else:
            quit()



print "Welcome to PiStation version 1.0"
time.sleep(2)
os.system("clear")
print "Would you like to broadcast through a microphone \nor a file type such as WAV or mp3?"
morf = raw_input("\nType M for Microphone or F for File Type\n").lower()
if morf == "f":
    
    check2 = raw_input("Press enter to continue...").lower()
    if check2 == "continue":
        os.system("clear")
        countdownspec()
        os.system("clear")
        print "BYPASS MODE\nSOME FEATURES MAY NOT WORK IN THIS MODE"
        time.sleep(2)
        os.system("clear")
        print "Please choose a frequency between 87.1 and 108.1"
    
        freq = float(raw_input()) #Frequency the RPI will play | float is used for numbers with decimals
    
        if freq <=  87.1 : #Keep the frequency above 87.1
            print "\nPlease keep the frequency above 87.1"
            quit()
    
        elif freq >= 108.2 : #Keep the frequency below 108.1
            print "\nPlease keep the frequency below 108.1"
            quit()

        else:
            os.system("clear")
            print "\nPlease give the the directory or your song ending with the file type \nEX. /folder1/favoritesong.WAV\n"
            time.sleep(.5)
            print "Not sure what directory your song is in? Type, 'browse' to look around your directories otherwise press enter"
            q1 = raw_input("\n").lower()
            if q1 == "browse":
                os.system("ls")
                print "\nType the folder you would like to go into"
                q2 = raw_input("\n") #folder 1
                os.chdir(q2)
                os.system("ls")
                q3 = raw_input("\nPlease type the song that you would like, with the ending. \nEX. Favoritesong.WAV\n\n") #song name
                os.chdir("../")
                direct = (q2 + "/" + q3)
                #ftype - file type
                #ftype 1 - WAV file
                #ftype 2 - mp3 file
                ftype11 = ".WAV" in direct
                ftype12 = ".wav" in direct
                ftype21 = ".mp3" in direct
                ftype22 = ".MP3" in direct
            
                if ftype11 or ftype12 == True:
                    if ftype11 == True:
                        ftwav()
                    elif ftype11 == False:
                        if ftype12 == True:
                            ftwav()
                        else:
                            time.sleep(3.5)
                            print "error 256"
                            print error256
                            time.sleep(2)
                            quit()

                        #--------------------------
                elif ftype11 or ftype12 == False:
                    if ftype21 == True:
                        ftmp3()
                    elif ftype21 == False:
                        if ftype22 == True:
                            ftmp3()
                        else:
                            time.sleep(3.5)
                            print "error256"
                            print error256
                            time.sleep(2)
                            print rebootask
                            ask1 = raw_input("Y/N").lower()
                            if ask1 == "y":
                                os.system("python pistation.py")
                            else:
                                quit()
            else:
                direct = raw_input("Enter your directory")
            
                #ftype - file type
                #ftype 1 - WAV file
                #ftype 2 - mp3 file
                ftype11 = ".WAV" in direct
                ftype12 = ".wav" in direct
                ftype21 = ".mp3" in direct
                ftype22 = ".MP3" in direct
            
                if ftype11 or ftype12 == True:
                    if ftype11 == True:
                        os.system("clear")
                        print "We have issuse working with WAV files.  It is reccomended that you use an mp3 file instead"
                        print "Does the song sound to fast, slow, or just not playing at all? Check the README files."
                        check1 = os.system("sudo ./pifm " + direct + " " + str(freq) + " 22050 stereo")
                        rebootpro()
                    elif ftype11 == False:
                        if ftype12 == True:
                            os.system("clear")
                            print "We have issuse working with WAV files.  It is reccomended that you use an mp3 file instead"
                            print "Does the song sound to fast, slow, or just not playing at all? Check the README files."
                            check1 = os.system("sudo ./pifm " + direct + " " + str(freq) + " 22050 stereo")
                            rebootpro()
                        else:
                            time.sleep(3.5)
                            print "error 256"
                            print error256
                            time.sleep(2)
                            quit()
                elif ftype11 or ftype12 == False:
                    if ftype21 == True:
                        ftmp3()
                    elif ftype21 == False:
                        if ftype22 == True:
                            ftmp3()
                        else:
                            time.sleep(3.5)
                            print "error256"
                            print error256
                            time.sleep(2)
                            quit()
    else:
        check = os.system("ffmpeg")
        print check
        time.sleep(2)
        os.system("clear")
        if check == 256: #256 is the number recevied from typing ffmpeg in the command line
    
            print "Please choose a frequency between 87.1 and 108.1"
    
            freq = float(raw_input()) #Frequency the RPI will play | float is used for numbers with decimals
    
            if freq <=  87.1 : #Keep the frequency above 87.1
                print "\nPlease keep the frequency above 87.1"
                rebootpro()
    
            elif freq >= 108.2 : #Keep the frequency below 108.1
                print "\nPlease keep the frequency below 108.1"
                rebootpro()

            else:
                os.system("clear")
                print "\nPlease give the the directory or your song ending with the file type \nEX. /folder1/favoritesong.WAV\n"
                time.sleep(.5)
                print "Not sure what directory your song is in? Type, 'browse' to look around your directories otherwise press enter"
                q1 = raw_input("\n").lower()
                if q1 == "browse":
                    os.system("ls")
                    print "\nType the folder you would like to go into"
                    q2 = raw_input("\n") #folder 1
                    os.chdir(q2)
                    os.system("ls")
                    q3 = raw_input("\nPlease type the song that you would like, with the ending. \nEX. Favoritesong.WAV\n\n") #song name
                    os.chdir("../")
                    direct = (q2 + "/" + q3)
                    #ftype - file type
                    #ftype 1 - WAV file
                    #ftype 2 - mp3 file
                    ftype11 = ".WAV" in direct
                    ftype12 = ".wav" in direct
                    ftype21 = ".mp3" in direct
                    ftype22 = ".MP3" in direct
            
                    if ftype11 or ftype12 == True:
                        if ftype11 == True:
                            ftwav()
                        elif ftype11 == False:
                            if ftype12 == True:
                                ftwav()
                            else:
                                time.sleep(3.5)
                                print "error 256"
                                print error256
                                time.sleep(2)
                                quit()
    
                        #--------------------------
                    elif ftype11 or ftype12 == False:
                        if ftype21 == True:
                            ftmp3()
                        elif ftype21 == False:
                            if ftype22 == True:
                                ftmp3()
                            else:
                                time.sleep(3.5)
                                print "error256"
                                print error256
                                time.sleep(2)
                                print rebootask
                                ask1 = raw_input("Y/N").lower()
                                if ask1 == "y":
                                    os.system("python pistationpy")
                                else:
                                    quit()
                else:
                    direct = raw_input("Type your directory\n")
            
                    #ftype - file type
                    #ftype 1 - WAV file
                    #ftype 2 - mp3 file
                    ftype11 = ".WAV" in direct
                    ftype12 = ".wav" in direct
                    ftype21 = ".mp3" in direct
                    ftype22 = ".MP3" in direct
            
                    if ftype11 or ftype12 == True:
                        if ftype11 == True:
                            os.system("clear")
                            print "Does the song sound to fast, slow, or just not playing at all? Check the README files."
                            check1 = os.system("sudo ./pifm " + direct + " " + str(freq) + " 22050 stereo")
                            rebootpro()
                        elif ftype11 == False:
                            if ftype12 == True:
                                os.system("clear")
                                print "Does the song sound to fast, slow, or just not playing at all? Check the README files."
                                check1 = os.system("sudo ./pifm " + direct + " " + str(freq) + " 22050 stereo")
                                rebootpro()
                            else:
                                time.sleep(3.5)
                                print "error 256"
                                print error256
                                time.sleep(2)
                                quit()
                    elif ftype11 or ftype12 == False:
                        if ftype21 == True:
                            ftmp3()
                        elif ftype21 == False:
                            if ftype22 == True:
                                ftmp3()
                            else:
                                time.sleep(3.5)
                                print "error256"
                                print error256
                                time.sleep(2)
                                quit()
        elif check == 32512:#32512 is the number recevied after typing ffmpeg in the command line without ffmpeg installed
            print error1
            countdown()
        else:
            print error2
            countdown()
if morf == "m":
    print "Please choose a frequency between 87.1 and 108.1"
    
    freq = float(raw_input()) #Frequency the RPI will play | float is used for numbers with decimals
    
    if freq <=  87.1 : #Keep the frequency above 87.1
        print "\nPlease keep the frequency above 87.1"
        quit()
    
    elif freq >= 108.2 : #Keep the frequency below 108.1
        print "\nPlease keep the frequency below 108.1"
        quit()

    else:
        os.system("arecord -d0 -c2 -f S16_LE -r 22050 -twav -D copy | sudo ./pifm - " + str(freq))
        rebootpro()

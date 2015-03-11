# PiStation
Transmit audio files (.wav or .mp3) across the FM band, listen to your music anywhere near you!

--------------
Instructions
--------------

Using the program is simple!  
Install PiFM and other required software by running the PiStationInstall.py <code>sudo python ./PiStationInstall.py</code>  

Proceed to run the file PiStation2 <code>sudo python ./PiStation2.py</code>  

After the file is up and running you will be asked to type in the song name (filename), be sure you DO NOT type in the path, you only need to type in the filename (with the extension MP3 or WAV).  

Then type in the station that you would like it to play on (frequency), after that you will hear you song over the radio on that frequency.

--------------
About the Program and What it Does
--------------

The code used in the program is <code>ffmpeg -i input.mp3 -f s16le -ar 22.05k -ac 1 - | sudo ./pifm - 99.9</code> for MP3's and <code>sudo ./pifm left_right.wav 103.3 22050 stereo</code> for WAV files.  The program will automatically decide weather to play it as a WAV or MP3 file.  As of now, these are the only two files supported.  

WAV files must be in the following format: 16 bit (mono or stereo) 22050 hz (generaly these are fine as-is, but you may need to convert it if it doesn't mach the required specs.)  Anything below 16 bits will work as well.

The Raspberry Pi can handle anywhere from 1MHz to 250MHz, however I limited it in the code to 87.1 and 108.1 beacuse generaly radio bands don't go past these numbers.  There is also majorly restricted frequencies in there like, 121.5 and 243.0 (military aircraft).  You can remove this block by commenting out the code.

The PiStation allows you to use the code (from icrobotics link below) in a more simple way, simply load your music
onto your Pi, and play!

http://www.icrobotics.co.uk/wiki/index.php/Turning_the_Raspberry_Pi_Into_an_FM_Transmitter

--------------

I apreciate all the help, and encourage updates to this program!  I still have a lot to learn, so any help would be awesome!

Have fun with your Pi!

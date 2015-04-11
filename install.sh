#!/bin/bash

CURRENT_DIR="`pwd`"

echo $CURRENT_DIR

if [ -f /usr/bin/ffmpeg]; then
	echo ""
else
	echo "NOTE: mp3 support requires ffmpeg"
fi

if [ -f $CURRENT_DIR/pifm]; then
	echo ""
else
	echo "Grabbing required dependancies"
	
	echo `wget http://omattos.com/pifm.tar.gz`
	echo `tar -xzf pifm.tar.gz`
	echo `rm pifm.tar.gz pifm.c PiFm.pyc sound.wav left_right.wav`
fi

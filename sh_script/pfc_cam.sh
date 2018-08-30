#!/bin/bash

DATE=`date "+%Y-%m-%d_%H_%M_%S"`

fswebcam -r 2594x1944 --no-banner -S 50 /home/pi/PFC/imgs/$DATE.jpg
raspistill -vf -o /home/pi/PFC/imgs/$DATE.jpg

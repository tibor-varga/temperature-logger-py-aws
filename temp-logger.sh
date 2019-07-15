#!/bin/sh
d=`/bin/date +%Y-%m-%d`
sudo /usr/bin/python /home/pi/temperature-logger-py-aws/temp-logger.py | /bin/grep rpi >> "/home/pi/temperature-logger-py-aws/logs/temp_rpi1_$d.log"

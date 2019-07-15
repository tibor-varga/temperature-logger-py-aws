#!/bin/sh
d=`/bin/date +%Y-%m-%d`
sudo /usr/local/bin/aws s3 cp "/home/pi/temperature-logger-py-aws/temp_rpi2_$d.log" s3://bbaws-temperature/

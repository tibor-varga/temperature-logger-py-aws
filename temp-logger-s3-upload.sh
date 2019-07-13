#!/bin/sh
d=`/bin/date +%Y-%m-%d`
sudo /usr/local/bin/aws s3 cp "/home/pi/temp_$d.log" s3://bbaws-temperature/

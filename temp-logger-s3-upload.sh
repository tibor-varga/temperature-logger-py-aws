#!/bin/sh
d=`/bin/date +%Y-%m-%d`
sudo /usr/local/bin/aws s3 sync "/home/pi/temperature-logger-py-aws/logs" s3://bbaws-temperature/

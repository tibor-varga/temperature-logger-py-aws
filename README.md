# temperature-logger-py-aws
simple temperature logger with python and aws s3

1. checkout project
```
cd /home/pi
git clone https://github.com/tibor-varga/temperature-logger-py-aws.git
```
2. install hid api
```
apt-get install install libhidapi-libusb0
pip install hid==0.1.1
```
3. setup aws s3 bucket

4. setup aws credentials

5. setup crontab:
```
*/1 * * * *     root    /home/pi/temperature-logger-py-aws/temp-logger.sh >> /tmp/crontab.log
59 23 * * *     root    /home/pi/temperature-logger-py-aws/temp-logger-s3-upload.sh >> /tmp/crontab.log
```


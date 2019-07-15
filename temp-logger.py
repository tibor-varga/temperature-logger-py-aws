#!/usr/bin/python
# Module:   hid_test.py
# Author:   Wade Hampton
# Date:     n/a
# Notes:
# 1)  This requires the hidapi module and the hid lib to be loaded.
#     - load hid module, tested on Ubuntu:
#         apt-get install install libhidapi-libusb0
#         [includes keyboard support]
#         [alt is libhidapi-hidraw0 for raw devices]
#     - get the Python module:  https://pypi.python.org/pypi/hid/0.1.1
#     - extract and install the python module
#         tar xvzf hid-0.1.1.tar.gz
#     - install (root)
#         cd hid-0.1.1
#         python setup.py install
# 2)  Plug in a HID USB device and run this program
#     - if device is raw, you might be able to open by path
#     - use vid/pid for non-raw devices (works for keyboards)
# 3)  This may need to be run as root unless you change the
#     permissions on the HID device....
#

import hid
from datetime import datetime

# get list of HID devices connected to this computer
h=hid.enumerate()
#print "HID info=", h

# get path of first item
item=0
path=h[item]['path']
vid=h[item]['vendor_id']
pid=h[item]['product_id']

# open the device
try:
  d=hid.Device(vid=vid, pid=pid)
  r=d.read(30)
  id=str(ord(r[0])) + str(ord(r[1])) + str(ord(r[2]));
  grad = str(float((((ord(r[5]) & 0xff) << 8) | (ord(r[4]) & 0xff)))/10)
  dateTimeObj = datetime.now()
  timestampStr = dateTimeObj.strftime("%Y-%m-%d_%H:%M:%S")

  print timestampStr + "	rpi1	id	"+id+"	"+ grad
  d.close()
# Read 2

  d=hid.Device(vid=vid, pid=pid)
  r=d.read(30)
  id=str(ord(r[0])) + str(ord(r[1])) + str(ord(r[2]));
  grad = str(float((((ord(r[5]) & 0xff) << 8) | (ord(r[4]) & 0xff)))/10)
  dateTimeObj = datetime.now()
  timestampStr = dateTimeObj.strftime("%Y-%m-%d_%H:%M:%S")

  print timestampStr + "	rpi1	id	"+id+"	"+ grad
  d.close()

        
except Exception, e:
    print "Exception, e=", e

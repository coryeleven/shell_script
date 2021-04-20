#!/bin/bash

ssh admin@55.13.116.23  sudo xdoctor --suite=local_hw >> /dev/null

source=`ssh admin@55.13.116.23 ls -rtlh /usr/local/xdoctor/archive/local_hw/|awk 'END {print}' |awk '{print $NF}'`
rm -rf /tmp/data.xml

scp -r admin@55.13.116.23:/usr/local/xdoctor/archive/local_hw/$source/data.xml /tmp/ >> /dev/null

#error_log=$(/usr/bin/python /home/qadmsom/psu.py  "/tmp/data.xml")
#echo "--------------------------------------"
#echo "$error_log"

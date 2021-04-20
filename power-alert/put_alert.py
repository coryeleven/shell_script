# coding:utf-8
import datetime
import time
import json
import urllib
import xml.etree.ElementTree as ET

Time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+0800")
root = ET.parse('/tmp/data.xml').getroot()
url = "http://172.24.143.242:8080"
for node in root.findall("collection[@name='all.cs_hal']/node"):
    for psu in node.findall("sensor[@type='PSU']/type[@entity='Power Supply']/item"):
        if psu.attrib['status'] != "OK":
            IP = node.attrib['name']
            Status = psu.attrib['status']
            Hostname = node.find('overview').get('name')
            result = {
                "agent":"nbu",
                "event_id":"ecspsu_10_30436",
                "status": "0",
                "eventName":"对象存储ECS监控告警",
                "eventTime": Time,
                "ipAddress":"192.168.1.101",  
                "host":"dg01dbadm02",
                "severity":"3",
                "summary":"主机名:" + node.find('overview').get('name') + ", IP:" + node.attrib['name'] +", 电源FAIL,系统当前本地时间:"  + Time,
                "type":"1"
            }
            data = json.dumps(result)
            print (data)
            res = urllib2.urlopen(url, data.encode()).read()
            print (res)

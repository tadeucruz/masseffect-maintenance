#!/usr/bin/env python3

import requests

from libs.personalConfig import config, closePersonalConfig
from libs.personalLogger import logger

username_dnsomatic = config['DNSOMATIC']['username']
password_dnsomatic = config['DNSOMATIC']['password']
oldIp = config['DNSOMATIC']['myIP']

if not str(username_dnsomatic):
    logger.info("username_dnsomatic is not configure")
    exit(1)

if not str(password_dnsomatic):
    logger.info("password_dnsomatic is not configure")
    exit(1)

myIp = ""
logger.info("Getting the current IP")
try:
    r = requests.get('http://myip.dnsomatic.com/')
    if r.status_code == 200:
        myIp = r.text
    else:
        logger.info("Problem to find current IP")
except:
    logger.info("Problem with your network")
    exit(1)

logger.info("Old IP %s Current IP %s", oldIp, myIp)

if str(oldIp) != str(myIp):
    r = requests.get('https://updates.dnsomatic.com/nic/update?hostname=all.dnsomatic.com&myip=' + myIp,
                     auth=(username_dnsomatic, password_dnsomatic))
    if "good" in str(r.text):
        config.set("DNSOMATIC", "myIP", myIp)
        logger.info('IP update to ' + myIp + ' old IP was ' + oldIp)
else:
    logger.info("Doesn't need to update the IP")

closePersonalConfig()

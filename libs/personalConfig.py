#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()
config.read('config/masseffect-maintenance.ini')


def closePersonalConfig():
    with open('config/masseffect-maintenance.ini', 'w') as configfile:
        config.write(configfile)

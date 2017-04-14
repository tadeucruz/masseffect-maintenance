#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()
config.read('masseffect-maintenance.ini')


def closePersonalConfig():
    with open('masseffect-maintenance.ini', 'w') as configfile:
        config.write(configfile)

#!/usr/bin/env python3

import logging

logger = logging.getLogger('update-dnsomatic-application')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
logger.addHandler(ch)

#!/bin/bash

git clone https://github.com/Diaoul/subliminal.git /opt/subliminal
cd /opt/subliminal
python3 setup.py install
cd /
/usr/sbin/crond -f

exit 0
#!/usr/bin/env python
import subprocess
cmd=['./setup.py','test','-a','--debug']
with open('log.txt', 'w') as out:
    return_code = subprocess.call(cmd, stdout=out)


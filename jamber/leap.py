from __future__ import absolute_import
import os
import subprocess
from .base import amberbin

def run(command):
    fn = 'jamber_tmp.in'
    if 'quit' not in command:
        command = command + '\nquit'
    with open(fn, 'w') as fh:
        fh.write(command)
    build_command = '{} -f {}'.format(amberbin('tleap'), fn).split()
    subprocess.check_output(build_command)
    os.unlink(fn)

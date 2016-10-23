import os
import subprocess
from .base import amberbin

def run(command):
    root = 'tmp_jamber'
    nabin = root + '.nab'
    nabout = root + '.out'
    nabc = root + '.c'

    with open(nabin, 'w') as fh:
        fh.write(command)
    nab_bin = amberbin('nab')
    build_command = [
            nab_bin,
            nabin,
            '-o',
            nabout
    ]
    subprocess.check_output(build_command)
    subprocess.check_output(['./{}'.format(nabout)])
    os.unlink(nabin)
    os.unlink(nabout)
    os.unlink(nabc)


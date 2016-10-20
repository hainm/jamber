from __future__ import absolute_import
from subprocess import Popen
from .base import amberbin

def run(command):
    if 'sander' not in command:
        command = ' '.join((amberbin('sander'), command))
    return Popen(command.split())

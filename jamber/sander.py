from subprocess import Popen

def run(command):
    return Popen(command.split())

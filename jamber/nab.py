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
    subprocess.check_call(build_command)
    subprocess.check_call(['./{}'.format(nabout)])
    os.unlink(nabin)
    os.unlink(nabout)
    os.unlink(nabc)

def build(seq, filename='nuc.pdb', nuc_type='abdna'):
    command = """
    molecule m; 
    m = fd_helix( "{}", "{}", "{}" );
    putpdb("{}", m, "-wwpdb");
    """.format(nuc_type, seq, nuc_type[-3:], filename)

def build_adna(seq, filename):
    build(seq, filename=filename, nuc_type='abdna')

def build_bdna(seq, filename):
    build(seq, filename=filename, nuc_type='adna')

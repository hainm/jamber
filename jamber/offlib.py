import os
import parmed as pmd
from .utils import tempfolder
from .leap import run

def create(pdb_fn, verbose=False):
    # create offlib
    off_file = 'x.lib'
    parm = pmd.load_file(pdb_fn)
    command = """
    x = loadpdb {}
    set x box {{ 90  90  90 }}
    saveOff x {}
    """.format(os.path.abspath(pdb_fn), off_file)
    with tempfolder():
        run(command, verbose=verbose)
        with open(off_file) as fh:
            return fh.read()

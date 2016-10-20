import os
import time
from jamber import sander
from jamber.utils import tempfolder

# local
from utils import get_fn

def test_sander():
    prmtop = get_fn('peptide.top')
    min_r = get_fn('min.rst7')
    mdin = get_fn('md.in')
    with tempfolder():
        command = '-O -p {prmtop} -c {min_r} -i {mdin}'.format(prmtop=prmtop, min_r=min_r,
                mdin=mdin) 
        sander.run(command)
        # wait a bit for output
        time.sleep(2)
        assert os.path.exists('mdinfo')

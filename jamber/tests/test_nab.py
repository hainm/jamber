import os
import numpy as np
from numpy.testing import assert_almost_equal as aa_eq
import parmed as pmd
import pytraj as pt
from jamber import nab
from jamber.base import amberbin
from jamber.utils import tempfolder
from jamber import nab, leap
from jamber import builder

try:
    nabin = amberbin('nab')
except AssertionError:
    nabin = None


def test_nab():
    fn = 'nuc.pdb'
    with tempfolder():
        nab.run("""
        molecule m; 
        m = fd_helix( "abdna", "aaaaaaaaaa", "dna" );
        putpdb("nuc.pdb", m, "-wwpdb");
        """)

        root = 'tmp_jamber'
        assert not os.path.exists(root + '.nab')
        assert not os.path.exists(root + '.c')
        assert not os.path.exists(root + '.out')

        parm = pmd.load_file(fn)
        assert len(parm.atoms) == 638

def test_nab_bdna():
    with tempfolder():
        traj = builder.build_bdna('AAAAAAAAAA')
        nu = pt.nastruct(traj)
        aa_eq(np.mean(nu.major[1]), [17.246,], decimal=3)
        aa_eq(np.mean(nu.minor[1]), [11.459,], decimal=3)

def test_nab_adna():
    with tempfolder():
        filename = 'nuc.pdb'
        traj = builder.build_adna('AAAAAAAAAA')
        nu = pt.nastruct(traj)
        aa_eq(np.mean(nu.major[1]), [15.721,], decimal=3)
        aa_eq(np.mean(nu.minor[1]), [18.398,], decimal=3)

def test_nab_arna():
    with tempfolder():
        filename = 'nuc.pdb'
        traj = builder.build_arna('AAAAAAAAAA')
        nu = pt.nastruct(traj)
        aa_eq(np.mean(nu.major[1]), [15.183,], decimal=3)
        aa_eq(np.mean(nu.minor[1]), [18.804,], decimal=3)

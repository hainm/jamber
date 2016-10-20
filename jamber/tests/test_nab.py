import os
import parmed as pmd
from jamber import nab
from jamber.utils import tempfolder

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

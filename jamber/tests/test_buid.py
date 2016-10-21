from numpy.testing import assert_almost_equal as aa_eq
from jamber import builder
from jamber.utils import get_fn
import pytraj as pt

def test_build():
    seq = "ALA ALA ALA ALA ALA ALA ALA ALA ALA ALA"

    def assert_build(ss_type, seq=seq):
        cm = '{}:1-10'.format(ss_type)
        traj = builder.build_protein(seq, [cm])
        # traj.save('test.pdb', overwrite=True)
        pdb_fn = get_fn('builder/ala10_{}.pdb'.format(ss_type))
        saved_traj = pt.load(pdb_fn)
        aa_eq(traj.xyz, saved_traj.xyz, decimal=3)

    assert_build('alpha', seq=seq)
    assert_build('hairpin', seq=seq)

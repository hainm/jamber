import numpy as np
import parmed as pmd
import pytraj
from jamber import add_to_box
from jamber.utils import get_fn

def test_add_to_box():
    pdb_fn = get_fn('builder/ala10_hairpin.pdb')
    wat_fn = get_fn('water.pdb')

    traj = pytraj.load(pdb_fn)
    traj.unitcells = np.array([[35.263, 41.846, 36.169, 90.00, 90.00, 90.00],])
    wat = pytraj.load(wat_fn)

    traj2 = add_to_box.pack(traj, wat, n_copies=100)
    assert traj2[':WAT'].top.n_residues == 100
    assert set(res.name for res in traj2[':WAT'].top.residues) == {'WAT'}

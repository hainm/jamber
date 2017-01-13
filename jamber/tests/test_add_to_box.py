import parmed as pmd
from jamber import add_to_box
from jamber.utils import get_fn

def test_solvate():
    pdb_fn = get_fn('builder/ala10_hairpin.pdb')
    wat_fn = get_fn('water.pdb')

    parm = pmd.load_file(pdb_fn)
    parm.box = [35.263, 41.846, 36.169, 90.00, 90.00, 90.00]
    wat = pmd.load_file(wat_fn)

    parm = add_to_box.pack(parm, wat, n_copies=100)
    assert len(parm[':WAT'].residues) == 100
    assert set(res.name for res in parm[':WAT'].residues) == {'WAT'}

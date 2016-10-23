from jamber import leap
from jamber.utils import tempfolder
import parmed as pmd

def test_leap():
    command = """
    source leaprc.protein.ff14SB
    seq = sequence {ALA ALA ALA}
    saveamberparm seq seq.prmtop seq.rst7
    """

    with tempfolder():
        leap.run(command)
        parm = pmd.load_file('seq.prmtop')
        assert len(parm.atoms) == 30

import pytraj as pt
from . import leap
from .utils import tempfolder

def build_protein(seq, command):
    '''

    Parameters
    ----------
    seq : protein sequence
    command : str or list of str
        pytraj command for building secondary structure for a given residue range

    Requires
    --------
    tleap, pytraj

    Examples
    --------
    >>> from jamber import build
    >>> # Ala10
    >>> seq = "ALA ALA ALA ALA ALA ALA ALA ALA ALA ALA"
    >>> traj = builder.build_protein(seq, ['alpha:1-10'])
    >>> # visualize in Jupyter notebook
    >>> traj.visualize()
    >>> # save to pdb file
    >>> traj.save("new.pdb")

    Returns
    -------
    pytraj.Trajectory
    '''
    pdb_fn = 'seq.pdb'
    leap_command = """
    source leaprc.protein.ff14SB
    x = sequence{%s}
    savepdb x %s
    """ % (seq, pdb_fn)

    with tempfolder():
        leap.build(leap_command)
        traj = pt.load(pdb_fn)
        return pt.make_structure(traj, command)

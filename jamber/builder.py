import os
import pytraj as pt
from . import leap
from .utils import tempfolder
from . import nab

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

    amberhome = os.getenv('AMBERHOME')
    if  os.path.exists(amberhome + '/dat/leap/cmd/leaprc.ff14SB'):
        leap_command = leap_command.replace('protein.ff14SB', 'ff14SB')

    with tempfolder():
        leap.build(leap_command)
        traj = pt.load(pdb_fn)
        return pt.make_structure(traj, command)

def _nab_build(seq, filename, nuc_type='abdna'):
    command = """
    molecule m; 
    m = fd_helix( "{}", "{}", "{}" );
    putpdb("{}", m, "-wwpdb");
    """.format(nuc_type, seq, nuc_type[-3:], filename)
    with tempfolder():
        nab.run(command)
        return pt.load(filename)

def build_adna(seq, filename='nuc.pdb'):
    return _nab_build(seq, filename=filename, nuc_type='adna')

def build_bdna(seq, filename='nuc.pdb'):
    return _nab_build(seq, filename=filename, nuc_type='abdna')

def build_arna(seq, filename='nuc.pdb'):
    return _nab_build(seq, filename=filename, nuc_type='arna')

import os
import pytraj as pt
from . import leap
from .utils import tempfolder
from . import nab

__all__ = [
        'build_protein',
        'build_adna',
        'build_bdna',
        'build_arna'
]

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

    command_str = ' '.join(command) if isinstance(command, list) else command

    amberhome = os.getenv('AMBERHOME')
    if  os.path.exists(amberhome + '/dat/leap/cmd/leaprc.ff14SB'):
        leap_command = leap_command.replace('protein.ff14SB', 'ff14SB')

    with tempfolder():
        leap.run(leap_command)
        traj = pt.load(pdb_fn)
        pt.make_structure(traj, command_str)
        return traj

def solvate(traj, water_model='tip3p', buffer=8.):
    fn = 'my.pdb'
    leap_command = """
    source leaprc.protein.ff14SB
    source leaprc.water.{water_model}
    pdb = loadpdb {input_pdb}
    solvateOct pdb TIP3PBOX {buffer}
    savepdb pdb {input_pdb}
    quit
    """.format(water_model=water_model, input_pdb=fn, buffer=buffer)

    with tempfolder():
        traj.save(fn, overwrite=True)
        leap.run(leap_command)
        return pt.load(fn)

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

import parmed
import pytraj
import numpy as np
from .base import amberbin
from .compat import StringIO
from .utils import tempfolder
import subprocess

def pack(traj, mol, n_copies, unitcells=None, ig=8888, grid_spacing=0.2):
    '''

    Parameters
    ----------
    traj : pytraj.Trajectory
    mol : pytraj.Trajectory
    unitcells : None or np.ndarray, dim=2
        if None, use box info from traj else use it
    n_copies : number of `mol`
    ig : int
        randome seed
    grid_spacing : float
    '''
    add_to_box_exe = amberbin('AddToBox') or 'AddToBox'
    input_pdb = 'input.pdb'
    mol_pdb = 'mol.pdb'
    out_pdb = 'out.pdb'

    assert mol.n_frames == 1
    
    total_n_atoms = traj.n_atoms + mol.n_atoms * n_copies
    new_traj_xyz = np.empty((traj.n_frames, total_n_atoms, 3), dtype='f8')

    with tempfolder():
        mol.save(mol_pdb, overwrite=True)
        for index, frame in enumerate(traj):
            pytraj.write_traj(input_pdb, traj=frame, top=traj.top, overwrite=True)
            parm = parmed.load_file(input_pdb)
            if unitcells is not None:
                parm.box = unitcells[index]
            else:
                assert frame.has_box(), 'must have box info'
                parm.box = frame.box
            # add remark 290
            parm.save(input_pdb, overwrite=True)
            command = [
                add_to_box_exe,
                '-c', input_pdb,
                '-a', mol_pdb,
                '-na', str(n_copies),
                '-IG', str(ig),
                '-G', str(grid_spacing),
                '-o', out_pdb
            ]
            try:
                subprocess.check_output(command, stderr=subprocess.STDOUT)
                new_traj_xyz[index] = pytraj.load(out_pdb).xyz
            except subprocess.CalledProcessError as e:
                return e.output.decode()
        top = pytraj.load_topology(out_pdb)
    return pytraj.Trajectory(xyz=new_traj_xyz, top=top)

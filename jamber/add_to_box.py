import parmed
from .base import amberbin
from .compat import StringIO
from .utils import tempfolder
import subprocess

def pack(parm, mol, n_copies, ig=8888, grid_spacing=0.2):
    add_to_box_exe = amberbin('AddToBox') or 'AddToBox'
    input_pdb = 'input.pdb'
    mol_pdb = 'mol.pdb'
    out_pdb = 'out.pdb'
    
    with tempfolder():
        parm.write_pdb(input_pdb)
        mol.write_pdb(mol_pdb)
        command = [
            add_to_box_exe,
            '-c', input_pdb,
            '-a', mol_pdb,
            '-na', str(n_copies),
            '-IG', str(ig),
            '-G', str(grid_spacing),
            '-o', out_pdb
        ]
        subprocess.check_output(command, stderr=subprocess.PIPE)
        return parmed.load_file(out_pdb)

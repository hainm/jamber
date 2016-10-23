import pytraj as pt
from jamber.builder import build_protein

seq = ' '.join(['ALA']*10)
print(seq)

traj = build_protein(seq, command=['alpha:1-10'])
print(traj)
print(pt.multidihedral(traj, dihedral_types='phi psi', dtype='dict'))

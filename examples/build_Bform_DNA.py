import pytraj as pt
from jamber.builder import build_bdna

seq = 'AAAAAAAAAA'
traj = build_bdna(seq)
nupar = pt.nastruct(traj)
print('major groove width', nupar.major[1])
print('minor groove width', nupar.minor[1])

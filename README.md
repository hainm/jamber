Wrapping some of AmberTools's programs for Jupyter notebook.

# Install
```bash
git clone https://github.com/hainm/jamber
cd jamber
python setup.py install
# If using ambertools
# amber.python setup.py install
```

# Example
- [notebooks](./examples)

- leap
```python
    from jamber import leap
    command = """
    source leaprc.protein.ff14SB
    seq = sequence {ALA ALA ALA}
    saveamberparm seq seq.prmtop seq.rst7
    """
    leap.build(command)
```

- nab
```python
from jamber import nab
nab.build_bdna(seq='AAAAAA', filename='nuc.pdb')
```

- build protein with given secondary structure

```python
from jamber.builder import build_protein
seq = 'ALA ALA ALA ALA ALA'
traj = build_protein(seq, ['alpha:1-5'])
# traj is pytraj.Trajectory
traj.save("new.pdb")
```
![](examples/images/builder_ala10.png)

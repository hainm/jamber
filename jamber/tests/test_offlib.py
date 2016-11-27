import os
from jamber import offlib
import unittest

amberhome = os.getenv('AMBERHOME', '')
fn = amberhome + '/AmberTools/test/leap/gaff_wildcrd.pdb'

@unittest.skipUnless(os.path.exists(fn), 'skip if {} not exits'.format(fn))
def test_offlib_create():
    assert os.path.exists(fn), '{} must exist'.format(fn)
    offlib.create(fn, verbose=True)

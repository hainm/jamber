import os
from contextlib import contextmanager
import tempfile
from shutil import rmtree

@contextmanager
def tempfolder():
  """run everything in temp folder
  """
  my_temp = tempfile.mkdtemp()
  cwd = os.getcwd()
  os.chdir(my_temp)
  yield
  os.chdir(cwd)
  rmtree(my_temp)

def get_fn(fn):
    this_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(this_path, 'tests', 'data', fn)

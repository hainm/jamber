import sys
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str
else:
    string_types = basestring

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .core import open_dataset, open_mfdataset
from . import plot

try:
    from . version import __version__
except ImportError:
    raise ImportError('gcpy was not properly installed; some functionality '
                      'may be not work. If installing from source code, '
                      'please re-install in place by running\n'
                      '$ pip install -e .'
                      '\nElse, please reinstall using your package manager.')

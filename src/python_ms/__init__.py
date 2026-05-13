"""Python equivalent of the JavaScript ms package."""

import importlib.metadata
import sys

from python_ms.ms import _ms

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"


# Courtesy of the Fuckit package
sys.modules[__name__] = _ms(__name__, __doc__)

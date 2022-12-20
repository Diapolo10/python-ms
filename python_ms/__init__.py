"""Python equivalent of the JavaScript ms package"""

import sys

from python_ms.ms import _ms

# Courtesy of the Fuckit package
sys.modules[__name__] = _ms(__name__, __doc__)

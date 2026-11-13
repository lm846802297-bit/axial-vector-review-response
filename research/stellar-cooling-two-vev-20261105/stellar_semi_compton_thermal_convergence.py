"""Two-VEV model adapter to the shared thermal quadrature-convergence driver."""
from pathlib import Path
import sys

MODEL_VARIANT = "Two-VEV model"
_HERE = Path(__file__).resolve().parent
_SHARED = _HERE.parent / "stellar-cooling-shared-20261105"
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
if str(_SHARED) not in sys.path:
    sys.path.insert(1, str(_SHARED))

from stellar_semi_compton_thermal_convergence_common import *

if __name__ == "__main__":
    main()

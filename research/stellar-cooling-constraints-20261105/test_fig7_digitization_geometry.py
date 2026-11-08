import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from audit_fig7_digitization_geometry import (
    ordered_polyline, legacy_polyline, transform_pdf_coordinates,
    visible_luminosity_mask,
)


class Fig7DigitizationGeometryTests(unittest.TestCase):
    def test_ordered_polyline_preserves_source_segment_order(self):
        drawing = {
            "items": [
                ("l", (1.0, 2.0), (2.0, 3.0)),
                ("l", (2.0, 3.0), (3.0, 1.0)),
            ]
        }
        np.testing.assert_allclose(
            ordered_polyline(drawing),
            np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 1.0]])
        )

    def test_discontinuous_source_path_is_rejected(self):
        drawing = {
            "items": [
                ("l", (1.0, 2.0), (2.0, 3.0)),
                ("l", (2.1, 3.0), (3.0, 1.0)),
            ]
        }
        with self.assertRaises(ValueError):
            ordered_polyline(drawing)

    def test_legacy_x_sort_does_not_drop_unique_monotonic_vertices(self):
        drawing = {
            "items": [
                ("l", (1.0, 2.0), (2.0, 3.0)),
                ("l", (2.0, 3.0), (3.0, 1.0)),
            ]
        }
        np.testing.assert_allclose(legacy_polyline(drawing), ordered_polyline(drawing))

    def test_axis_endpoints_map_to_pinned_physical_ranges(self):
        xy = np.array([
            [54.82951354980469, 195.54043579101562],
            [397.99951171875, 20.904434204101562],
        ])
        result = transform_pdf_coordinates(xy)
        np.testing.assert_allclose(result["alpha"], [1e-22, 1e-6], rtol=2e-14)
        np.testing.assert_allclose(
            result["luminosity_erg_s"], [1e52, 1e55], rtol=2e-14
        )
        np.testing.assert_allclose(
            result["g"], np.sqrt(4*np.pi*np.array([1e-22, 1e-6])),
            rtol=2e-14
        )

    def test_visible_mask_uses_the_published_luminosity_frame(self):
        transformed = {
            "luminosity_erg_s": np.array([0.99e52, 1.0e52, 1e53, 1.0e55, 1.01e55])
        }
        np.testing.assert_array_equal(
            visible_luminosity_mask(transformed),
            np.array([False, True, True, True, False])
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

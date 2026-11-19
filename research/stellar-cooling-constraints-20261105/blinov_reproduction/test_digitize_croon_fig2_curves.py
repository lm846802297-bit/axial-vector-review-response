import unittest

import numpy as np

try:
    from . import digitize_croon_fig2_curves as digitizer_module
except ImportError:
    import digitize_croon_fig2_curves as digitizer_module

MASS_LABELS = digitizer_module.MASS_LABELS
calibrate_axes = digitizer_module.calibrate_axes
digitize_points = digitizer_module.digitize_points
match_label_paths = digitizer_module.match_label_paths


def _path(index, rect, colour=(0.0, 0.0, 0.0), dashes="[] 0", width=0.5,
          points=None):
    return {
        "index": index,
        "rect": list(rect),
        "stroke_rgb": list(colour),
        "dashes": dashes,
        "width": width,
        "flattened_points": points or [[rect[0], rect[1]], [rect[2], rect[3]]],
    }


def _synthetic_axis_paths():
    paths = [
        _path(0, (10.0, 20.0, 10.0, 220.0)),
        _path(1, (410.0, 20.0, 410.0, 220.0)),
        _path(2, (10.0, 20.0, 410.0, 20.0)),
        _path(3, (10.0, 220.0, 410.0, 220.0)),
    ]
    for i, x in enumerate(np.linspace(10.0, 410.0, 6)):
        paths.append(_path(10+i, (x, 214.0, x, 220.0)))
    for i, y in enumerate(np.linspace(20.0, 220.0, 5)):
        paths.append(_path(20+i, (10.0, y, 16.0, y)))
    return paths


def _synthetic_labels_and_curves():
    spans = []
    paths = []
    for i, label in enumerate(MASS_LABELS):
        rgb = digitizer_module.MASS_STROKE_RGB[label]
        # The printed legend text is black; the path stroke carries the colour.
        spans.append({"text": label, "color": 0x000000})
        paths.append(_path(
            100+i, (20.0, 40.0+i, 220.0, 180.0-i),
            rgb, "[] 0", points=[[20.0, 100.0], [220.0, 180.0]]
        ))
    # A separate black dashed path represents the R_far=R_nu sensitivity.
    paths.append(_path(
        200, (20.0, 50.0, 220.0, 170.0), (0.0, 0.0, 0.0), "[3 2] 0",
        points=[[20.0, 50.0], [220.0, 170.0]]
    ))
    return spans, paths


class CroonFig2CurveDigitizationTests(unittest.TestCase):
    def test_axis_calibration_uses_all_major_ticks(self):
        axes = calibrate_axes(_synthetic_axis_paths())
        self.assertEqual(axes["x_major_tick_log10_g"], [-11.0, -9.0, -7.0, -5.0, -3.0, -1.0])
        self.assertEqual(axes["y_major_tick_log10_L"], [55.0, 54.0, 53.0, 52.0, 51.0])
        self.assertLess(axes["x_tick_fit_max_abs_residual_dex"], 1e-12)
        self.assertLess(axes["y_tick_fit_max_abs_residual_dex"], 1e-12)

    def test_mass_labels_match_distinct_in_plot_paths(self):
        spans, paths = _synthetic_labels_and_curves()
        matches = match_label_paths(spans, paths)
        self.assertEqual(set(matches), set(MASS_LABELS))
        indices = [matches[label]["path_index"] for label in MASS_LABELS]
        self.assertEqual(len(indices), len(set(indices)))
        self.assertEqual(matches["0.1 eV"]["path_index"], 105)

    def test_duplicate_path_match_is_rejected(self):
        original_labels = digitizer_module.MASS_LABELS
        original_palette = digitizer_module.MASS_STROKE_RGB
        try:
            digitizer_module.MASS_LABELS = ("200 MeV", "10 MeV")
            digitizer_module.MASS_STROKE_RGB = {
                "200 MeV": (1.0, 0.0, 0.0),
                "10 MeV": (1.0, 0.0, 0.0),
            }
            spans = [
                {"text": "200 MeV", "color": 0x000000},
                {"text": "10 MeV", "color": 0x000000},
            ]
            paths = [
                _path(1, (20.0, 40.0, 220.0, 180.0), (1.0, 0.0, 0.0)),
            ]
            with self.assertRaisesRegex(RuntimeError, "Ambiguous curve matching"):
                digitizer_module.match_label_paths(spans, paths)
        finally:
            digitizer_module.MASS_LABELS = original_labels
            digitizer_module.MASS_STROKE_RGB = original_palette


    def test_digitization_discards_points_outside_axes_and_maps_log_ticks(self):
        axes = {
            "plot_rect_pdf_points": [10.0, 20.0, 410.0, 220.0],
            "x_log10_g_from_pdf_x": {"slope": 0.025, "intercept": -11.25},
            "y_log10_L_from_pdf_y": {"slope": -0.02, "intercept": 55.4},
        }
        points = digitize_points(
            [[10.0, 20.0], [410.0, 220.0], [420.0, 100.0]], axes
        )
        self.assertEqual(len(points), 2)
        self.assertAlmostEqual(points[0]["log10_g"], -11.0)
        self.assertAlmostEqual(points[0]["log10_L_erg_s"], 55.0)
        self.assertAlmostEqual(points[1]["log10_g"], -1.0)
        self.assertAlmostEqual(points[1]["log10_L_erg_s"], 51.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

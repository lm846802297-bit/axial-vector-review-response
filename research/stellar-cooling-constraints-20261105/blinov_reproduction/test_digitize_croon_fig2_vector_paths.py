import unittest
from types import SimpleNamespace

import pymupdf

try:
    from .digitize_croon_fig2_vector_paths import bezier, flatten_drawing, find_figure_page
except ImportError:
    from digitize_croon_fig2_vector_paths import bezier, flatten_drawing, find_figure_page


class CroonFig2VectorExtractionTests(unittest.TestCase):
    def test_cubic_bezier_endpoints_and_midpoint(self):
        p0 = pymupdf.Point(0.0, 0.0)
        p1 = pymupdf.Point(0.0, 1.0)
        p2 = pymupdf.Point(1.0, 1.0)
        p3 = pymupdf.Point(1.0, 0.0)
        points = bezier(p0, p1, p2, p3, samples=2)
        self.assertEqual(points[0], [0.0, 0.0])
        self.assertEqual(points[-1], [1.0, 0.0])
        self.assertAlmostEqual(points[1][0], 0.5, places=14)
        self.assertAlmostEqual(points[1][1], 0.75, places=14)

    def test_flatten_drawing_preserves_connected_line_and_bezier(self):
        drawing = {
            "items": [
                ("l", pymupdf.Point(0, 0), pymupdf.Point(1, 0)),
                ("c", pymupdf.Point(1, 0), pymupdf.Point(1, 1),
                 pymupdf.Point(2, 1), pymupdf.Point(2, 0)),
            ]
        }
        points = flatten_drawing(drawing, bezier_samples=4)
        self.assertEqual(points[0], [0.0, 0.0])
        self.assertEqual(points[1], [1.0, 0.0])
        self.assertEqual(points[-1], [2.0, 0.0])
        self.assertEqual(len(points), 6)

    def test_caption_page_detection_ignores_ordinary_fig2_references(self):
        class Page:
            def __init__(self, text):
                self.text = text

            def get_text(self, mode):
                return self.text

        doc = [
            Page("The result is shown in Figure 2 in the next section."),
            Page("Figure 2: Luminosity due to Z-prime production."),
        ]
        index, text = find_figure_page(doc)
        self.assertEqual(index, 1)
        self.assertIn("Luminosity", text)

    def test_ambiguous_duplicate_captions_are_rejected(self):
        class Page:
            def get_text(self, mode):
                return "Figure 2: duplicated caption"

        with self.assertRaises(RuntimeError):
            find_figure_page([Page(), Page()])


if __name__ == "__main__":
    unittest.main(verbosity=2)

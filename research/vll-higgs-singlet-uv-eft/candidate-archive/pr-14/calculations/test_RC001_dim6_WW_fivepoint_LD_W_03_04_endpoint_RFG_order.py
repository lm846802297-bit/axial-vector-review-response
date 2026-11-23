import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).with_name("RC-001-dim6-WW-fivepoint-LD-W-03-04-endpoint-RFG-order.py")
SPEC = importlib.util.spec_from_file_location("ldw0304_order", PATH)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class LDW0304EndpointOrderTests(unittest.TestCase):
    def test_symbolic_endpoint_orders_and_conjugation(self):
        self.assertEqual(MOD.verify_symbolic_endpoint_orders(), 6)

    def test_he_spectator_is_k_independent(self):
        self.assertEqual(MOD.verify_he_spectator_independence(), 32)

    def test_rational_point_endpoints_and_rfg_are_distinct(self):
        k = [4, 1, 2, 1]
        q = [1, 2, 0, 1]
        p1 = [1, 0, 1, 0]
        p2 = [0, 1, 0, 2]
        p3 = [2, 1, 1, 1]
        result = MOD.audit_point(k, q, p1, p2, p3, 400)
        self.assertEqual(set(result), {"03", "04"})
        self.assertEqual(result["03"]["denominators"], (10, 8, 14, 11, -415))
        self.assertEqual(result["04"]["denominators"], (10, 8, -4, 3, -405))


if __name__ == "__main__":
    unittest.main()

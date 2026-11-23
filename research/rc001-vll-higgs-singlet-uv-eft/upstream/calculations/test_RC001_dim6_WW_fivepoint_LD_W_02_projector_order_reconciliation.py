#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest
HERE=pathlib.Path(__file__).resolve().parent
SOURCE=HERE/"RC-001-dim6-WW-fivepoint-LD-W-02-projector-order-reconciliation.py"
SPEC=importlib.util.spec_from_file_location("rc001_ldw02_projector_order",SOURCE)
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)

class TestLDW02ProjectorOrder(unittest.TestCase):
 def test_chiral_intertwining(self):
  self.assertEqual(MOD.verify_chiral_intertwining(),10)
 def test_actual_endpoint_reductions(self):
  checks,*_=MOD.rational_endpoint_projector_order()
  self.assertEqual(checks,128)
 def test_RFG_is_separate(self):
  self.assertEqual(MOD.verify_RFG_is_separate(),(16,16,16))
 def test_rational_denominators_and_currents(self):
  _,den,vk,vkap,*_=MOD.rational_endpoint_projector_order()
  self.assertTrue(all(x!=0 for x in den))
  self.assertEqual((vk,vkap),(-33,-18))
 def test_main_boundary(self):
  import contextlib,io
  out=io.StringIO()
  with contextlib.redirect_stdout(out): MOD.main()
  self.assertIn("no equality of single-W endpoints",out.getvalue())

if __name__=="__main__": unittest.main(verbosity=2)

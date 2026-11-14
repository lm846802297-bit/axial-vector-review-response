"""Regression: the complete tadpole-improved symbolic audit executes."""
from pathlib import Path
import subprocess
import sys
import unittest


class A4dRunTest(unittest.TestCase):
    def test_complete_audit_executes(self):
        script = Path(__file__).with_name('a4d_tadpole_improved_ss_kernel_audit.py')
        result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True, check=True)
        self.assertIn('Momentum-dependent UV pole after tadpole improvement', result.stdout)
        self.assertIn('PASS: exact cancellation identity', result.stdout)
        self.assertIn('LIMIT:', result.stdout)


if __name__ == '__main__':
    unittest.main()

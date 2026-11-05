"""Offline tests for raw Belle II supplement download validation."""
import hashlib
import unittest

from fetch_belleii_supplements import sha256_bytes, validate_payload


class SupplementFetchTests(unittest.TestCase):
    def test_sha256_is_reproducible(self):
        payload = b"mass_GeV,observed_UL_fb\\n3.6,1.2\\n"
        self.assertEqual(sha256_bytes(payload), hashlib.sha256(payload).hexdigest())

    def test_plain_text_and_csv_payloads_are_accepted(self):
        validate_payload(b"mass_GeV,observed_UL_fb\\n3.6,1.2\\n", "text/csv")
        validate_payload(b"mass  observed_UL\\n3.6  1.2\\n", "text/plain")

    def test_html_challenge_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_payload(b"<!doctype html><html>blocked</html>", "text/html")

    def test_empty_and_access_denied_payloads_are_rejected(self):
        with self.assertRaises(ValueError):
            validate_payload(b"", "text/plain")
        with self.assertRaises(ValueError):
            validate_payload(b"Access denied by robot check", "text/plain")


if __name__ == "__main__":
    unittest.main()

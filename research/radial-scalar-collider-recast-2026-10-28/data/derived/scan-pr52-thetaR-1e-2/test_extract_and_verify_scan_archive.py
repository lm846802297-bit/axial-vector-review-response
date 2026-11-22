"""Unit tests for the streaming scan archive verifier."""
from __future__ import annotations
import gzip
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from extract_and_verify_scan_archive import inspect_csv, sha256_file


class ScanArchiveVerifierTests(unittest.TestCase):
    def test_sha256_file_streaming(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "x.bin"
            path.write_bytes(b"abc" * 100)
            digest, size = sha256_file(path)
            self.assertEqual(digest, hashlib.sha256(b"abc" * 100).hexdigest())
            self.assertEqual(size, 300)

    def test_csv_shape_inspection(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "x.csv"
            path.write_text("a,b,c\n1,2,3\n4,5,6\n", encoding="utf-8")
            info = inspect_csv(path)
            self.assertEqual(info["row_count"], 2)
            self.assertEqual(info["column_count"], 3)
            self.assertEqual(info["bad_width_rows"], [])

    def test_gzip_crc_and_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "data.csv"
            archive = root / "data.csv.gz"
            source.write_text("a,b\n1,2\n", encoding="utf-8")
            with gzip.open(archive, "wb") as stream:
                stream.write(source.read_bytes())
            with gzip.open(archive, "rb") as stream:
                self.assertEqual(stream.read(), source.read_bytes())


if __name__ == "__main__":
    unittest.main()

import unittest
import sys
from fastapi.testclient import TestClient

sys.path.append("..")
from Tools import manager as m
from Server import server as s

client = TestClient(s.app)


class ToolsTestCase(unittest.TestCase):
    def test_crypto(self):
        self.assertEqual("test", m.decrypt(m.encrypt("test")))

    def test_hash(self):
        self.assertEqual("098f6bcd4621d373cade4e832627b4f6", m.hash("test", "md5"))
        self.assertEqual("a94a8fe5ccb19ba61c4c0873d391e987982fbbd3", m.hash("test", "sha1"))
        self.assertEqual("90a3ed9e32b2aaf4c61c410eb925426119e1a9dc53d4286ade99a809", m.hash("test", "sha224"))
        self.assertEqual("9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08", m.hash("test", "sha256"))
        self.assertEqual("768412320f7b0aa5812fce428dc4706b3cae50e02a64caa16a782249bfe8efc4b7ef1ccb126255d196047dfedf17a0a9", m.hash("test", "sha384"))
        self.assertEqual("ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff", m.hash("test", "sha512"))
        self.assertEqual("9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08", m.hash("test"))

        self.assertRaises(ValueError, m.hash, "test", "sha256a")
        self.assertNotEqual(m.hash("test", "sha256"), m.hash("testa", "sha256"))


class ServerTestCase(unittest.TestCase):
    def test_ping(self):
        response = client.get("/ping")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "pong")

    def test_crypto(self):
        response = client.get("/crypto/encrypt?text=test")
        self.assertEqual(response.status_code, 200)
        encrypted = response.json()["encrypted"]
        key = response.json()["key"]
        response = client.get("/crypto/decrypt?text=" + encrypted + "&key=" + key)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "test")

    def test_hash(self):
        response = client.get("/crypto/hash?text=test&mode=sha256")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08")
        response = client.get("/crypto/hash?text=test")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08")
        response = client.get("/crypto/hash?text=test&mode=md5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "098f6bcd4621d373cade4e832627b4f6")

        self.assertRaises(ValueError, client.get, "/crypto/hash?text=test&mode=sha256a")


if __name__ == '__main__':
    unittest.main()

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


class ServerTestCase(unittest.TestCase):
    def test_ping(self):
        response = client.get("/ping")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "pong")

    def test_crypto(self):
        response = client.get("/crypto/encrypt?to_encrypt=test")
        self.assertEqual(response.status_code, 200)
        encrypted = response.json()["encrypted"]
        key = response.json()["key"]
        response = client.get("/crypto/decrypt?to_decrypt=" + encrypted + "&key=" + key)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "test")


if __name__ == '__main__':
    unittest.main()

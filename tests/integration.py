# http probes 
import requests
import unittest

class TestNginxIntegration(unittest.TestCase):
    BASE_URL = "http://localhost:8080"

    def test_root_returns_index_html(self):
        resp = requests.get(f"{self.BASE_URL}/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("<title>Hello World</title>", resp.text)
        self.assertIn("<h1>Hello, world</h1>", resp.text)
        self.assertIn("Served by Tylers nginx server", resp.text)

    def test_index_html_available(self):
        resp = requests.get(f"{self.BASE_URL}/index.html")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Hello", resp.text)

    def test_health_endpoint(self):
        resp = requests.get(f"{self.BASE_URL}/health")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.text.strip(), "OK")

    def test_nonexistent_returns_404(self):
        resp = requests.get(f"{self.BASE_URL}/doesnotexist")
        self.assertEqual(resp.status_code, 404)

if __name__ == "__main__":
    unittest.main()
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class IndexHtmlTests(unittest.TestCase):
    def setUp(self):
        self.html = (ROOT / "html" / "index.html").read_text()

    def test_title(self):
        self.assertIn("<title>Hello World</title>", self.html)

    def test_heading(self):
        self.assertIn("<h1>Hello, world</h1>", self.html)

    def test_served_by_line(self):
        self.assertIn("Served by Tylers nginx server", self.html)


class NginxConfigTests(unittest.TestCase):
    def setUp(self):
        self.conf = (ROOT / "nginx.conf").read_text()

    def test_listens_on_port_80(self):
        self.assertIn("listen 80;", self.conf)

    def test_serves_index_html(self):
        self.assertIn("root /usr/share/nginx/html;", self.conf)
        self.assertIn("index index.html;", self.conf)


if __name__ == "__main__":
    unittest.main()

import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_includes_name(self):
        self.assertIn("world", greet("world"))

    def test_starts_with_hello(self):
        self.assertTrue(greet("world").startswith("Hello,"))


if __name__ == "__main__":
    unittest.main()

import unittest


class SampleTestCase(unittest.TestCase):
    def setUp(self):
        print("setup init")
        self.a = 10

    def test_1(self):
        print("testing")

    def tearDown(self):
        print("setup init")
        self.a = 0


if __name__ == "__main__":
    unittest.main()

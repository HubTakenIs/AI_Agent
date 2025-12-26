import unittest
from functions.get_files_info import get_files_info

class TestClass(unittest.TestCase):

    def test_calculator_dir(self):
        results = get_files_info("calculator", ".")
        print(results)
        self.assertIsNotNone(results)

    def test_calculator_pkg(self):
        results = get_files_info("calculator", "pkg")
        print(results)
        self.assertIsNotNone(results)

    def test_calculator_bin(self):
        results = get_files_info("calculator", "/bin")
        print(results)
        self.assertIsNotNone(results)

    def test_calculator_cd_back(self):
        results = get_files_info("calculator", "../")
        print(results)
        self.assertIsNotNone(results)


if __name__ == '__main__':
    unittest.main()
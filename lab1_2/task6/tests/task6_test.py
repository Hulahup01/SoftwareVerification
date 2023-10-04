import unittest
from lab1.task6.task6 import download_file


class Task6Test(unittest.TestCase):
    def test_download_1(self):
        self.assertEqual(
            download_file("https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe",
                          "D:\\Content\\Media"),
            True)

    def test_download_2(self):
        self.assertEqual(
            download_file("https://www.python.org/ftp/python/rwgar.exe",
                          "D:\\Content\\Media"),
            False)

    def test_download_3(self):
        self.assertEqual(
            download_file("https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe",
                          "D:\\Content\\Media\\COCO"),
            False)


if __name__ == '__main__':
    unittest.main()

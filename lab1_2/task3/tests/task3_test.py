import unittest
from lab1.task3.task3 import area_calc


class Task3Test(unittest.TestCase):

    def test_area_calc_1(self):
        self.assertEqual(area_calc(1, 1), 1)

    def test_age_stat_4(self):
        self.assertEqual(area_calc(100000, 200000), 20000000000)

    def test_age_stat_5(self):
        self.assertEqual(area_calc(10523253352, 25325322350), 266504783310118017200)


if __name__ == '__main__':
    unittest.main()

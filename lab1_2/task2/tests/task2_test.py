import unittest
from lab1.task2.task2 import age_statistic


class Task2Test(unittest.TestCase):

    def test_age_stat_1(self):
        people = [
            ("mark", "lol", 12),
        ]
        self.assertEqual(age_statistic(people), (12, 12, 12))

    def test_age_stat_2(self):
        people = [
            ("mark", "lol", 10),
            ("jack", "pop", 20),
        ]
        self.assertEqual(age_statistic(people), (10, 20, 15))

    def test_age_stat_3(self):
        people = [
            ("mark", "lol", 10),
            ("jack", "pop", 20),
            ("jack", "pop", 20),
            ("mark", "lol", 10),
            ("jack", "pop", 20),
            ("jack", "pop", 20),
            ("mark", "lol", 10),
            ("jack", "pop", 20),
            ("jack", "pop", 20),
            ("mark", "lol", 10),
        ]
        self.assertEqual(age_statistic(people), (10, 20, 16))


if __name__ == '__main__':
    unittest.main()

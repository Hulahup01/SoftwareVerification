import unittest
from lab1.task5.task5 import search_files_with_extension


class Task5Test(unittest.TestCase):
    def test_search_1(self):
        self.assertEqual(search_files_with_extension(
            "D:\\Content\\Media\\WallPapers\\Default 11", ".png"),
            ['D:\\Content\\Media\\WallPapers\\Default 11\\default_11_1.png',
             'D:\\Content\\Media\\WallPapers\\Default 11\\default_11_2.png',
             'D:\\Content\\Media\\WallPapers\\Default 11\\default_11_3.png'])

    def test_search_2(self):
        self.assertEqual(search_files_with_extension("D:\\ff", ".png"),  [])

    def test_search_3(self):
        self.assertEqual(search_files_with_extension(
            "D:\\Content\\Media", ".png"),
            ['D:\\Content\\Media\\Pictures\\Снимок экрана 2023-03-24 023606.png',
             'D:\\Content\\Media\\Pictures\\Снимок экрана 2023-03-24 023650.png',
             'D:\\Content\\Media\\WallPapers\\0709b138-e9c2-47c3-82f8-0de004ff1f77.png',
             'D:\\Content\\Media\\WallPapers\\10.png',
             'D:\\Content\\Media\\WallPapers\\11.png',
             'D:\\Content\\Media\\WallPapers\\14.png',
             'D:\\Content\\Media\\WallPapers\\15.png',
             'D:\\Content\\Media\\WallPapers\\16.png',
             'D:\\Content\\Media\\WallPapers\\17.png',
             'D:\\Content\\Media\\WallPapers\\18.png',
             'D:\\Content\\Media\\WallPapers\\2.png',
             'D:\\Content\\Media\\WallPapers\\22.png',
             'D:\\Content\\Media\\WallPapers\\23.png',
             'D:\\Content\\Media\\WallPapers\\24.png',
             'D:\\Content\\Media\\WallPapers\\27.png',
             'D:\\Content\\Media\\WallPapers\\29.png',
             'D:\\Content\\Media\\WallPapers\\3.png',
             'D:\\Content\\Media\\WallPapers\\30.png',
             'D:\\Content\\Media\\WallPapers\\31.png',
             'D:\\Content\\Media\\WallPapers\\33.png',
             'D:\\Content\\Media\\WallPapers\\4.png',
             'D:\\Content\\Media\\WallPapers\\5.png',
             'D:\\Content\\Media\\WallPapers\\Summertime Night.png',
             'D:\\Content\\Media\\WallPapers\\Summertime Sunset.png',
             'D:\\Content\\Media\\WallPapers\\Surf Dark.png',
             'D:\\Content\\Media\\WallPapers\\Surf.png',
             'D:\\Content\\Media\\WallPapers\\Default 11\\default_11_1.png',
             'D:\\Content\\Media\\WallPapers\\Default 11\\default_11_2.png',
             'D:\\Content\\Media\\WallPapers\\Default 11\\default_11_3.png',
             'D:\\Content\\Media\\WallPapers\\Home\\1.png',
             'D:\\Content\\Media\\WallPapers\\Home\\2.png',
             'D:\\Content\\Media\\WallPapers\\Home\\3.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\After All.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\Equation Of Time wide.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\Equation Of Time.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\Forest Kingdom.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\Imagenero.png',
             "D:\\Content\\Media\\WallPapers\\Lofi\\Les jours d'aprКs.png",
             'D:\\Content\\Media\\WallPapers\\Lofi\\Morning Coffee.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\new beginnings.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\Passing By.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\Quietude.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\Sunday Morning.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\The Inner Light.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\The Spirit Within.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\Thin Lines.png',
             'D:\\Content\\Media\\WallPapers\\Lofi\\Three of Us.png',
             'D:\\Content\\Media\\WallPapers\\Official\\BW.png',
             'D:\\Content\\Media\\WallPapers\\Official\\C.png'])


if __name__ == '__main__':
    unittest.main()

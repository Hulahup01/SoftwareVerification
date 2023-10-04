import unittest
from bs4 import BeautifulSoup


def read_html_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


class TestGradientHTML(unittest.TestCase):

    def setUp(self):
        self.html_content = read_html_file('../gradient.html')
        self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def test_num_rows(self):
        rows = self.soup.table.find_all('tr')
        self.assertEqual(len(rows), 256)

    def test_row_colors(self):
        rows = self.soup.table.find_all('tr')
        for i, row in enumerate(rows):
            gradient_color = "rgb({}, {}, {})".format(
                int(255 - i * (255 / 255)),
                int(255 - i * (255 / 255)),
                int(255 - i * (255 / 255))
            )
            self.assertEqual(row['style'], 'background-color: {};'.format(gradient_color))


if __name__ == '__main__':
    unittest.main()

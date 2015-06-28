import unittest
import twothirds

class TestData(unittest.TestCase):
    def test_initialisation_from_xls_file(self):
        file_name = 'game.xls'
        data = twothirds.Data(file_name)
        self.assertEqual(file_name, data.filename)
        self.assertEqual('excel', data.filetype)

    def test_initialisation_from_csv_file(self):
        file_name = 'game.csv'
        data = twothirds.Data(file_name)
        self.assertEqual(file_name, data.filename)
        self.assertEqual('csv', data.filetype)

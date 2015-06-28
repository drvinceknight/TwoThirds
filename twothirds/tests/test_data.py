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

    def test_import_from_csv_file(self):
        file_name = 'twothirds/tests/test_data/game.csv'
        data = twothirds.Data(file_name)
        data.read()
        self.assertEqual(['Name', 'Guess'], list(data.df.columns.values))
        self.assertEqual(['A', 'B', 'C'], list(data.df['Name']))
        self.assertEqual([1, 2, 3], list(data.df['Guess']))
        self.assertEqual((3, 2), data.df.shape)

    def test_import_from_excel_file(self):
        file_name = 'twothirds/tests/test_data/game.xls'
        data = twothirds.Data(file_name)
        data.read()
        self.assertEqual(['A', 'B', 'C'], list(data.df['Name']))
        self.assertEqual([1, 2, 3], list(data.df['Guess']))
        self.assertEqual((3, 2), data.df.shape)

    def test_import_from_csv_file_with_no_names(self):
        file_name = 'twothirds/tests/test_data/game1.csv'
        data = twothirds.Data(file_name)
        data.read()
        self.assertEqual(['Guess'], list(data.df.columns.values))
        self.assertEqual([1, 2, 3], list(data.df['Guess']))
        self.assertEqual((3, 1), data.df.shape)

    def test_import_from_csv_file_with_multiple_guesses(self):
        file_name = 'twothirds/tests/test_data/game2.csv'
        data = twothirds.Data(file_name)
        data.read()
        self.assertEqual(['Name', 'Guess 1', 'Guess 2'], list(data.df.columns.values))
        self.assertEqual((3, 3), data.df.shape)
        self.assertEqual([1, 2, 3], list(data.df['Guess 1']))
        self.assertEqual([4, 5, 6], list(data.df['Guess 2']))

    def test_import_from_excel_file_with_multiple_guesses(self):
        file_name = 'twothirds/tests/test_data/game2.xlsx'
        data = twothirds.Data(file_name)
        data.read()
        self.assertEqual(['Name', 'Guess 1', 'Guess 2'], list(data.df.columns.values))
        self.assertEqual((3, 3), data.df.shape)
        self.assertEqual([1, 2, 3], list(data.df['Guess 1']))
        self.assertEqual([4, 5, 6], list(data.df['Guess 2']))

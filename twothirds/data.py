"""A module for the data import handler"""
import pandas

class Data:
    def __init__(self, filename):
        self.filename = filename
        if filename.endswith('.xls') or filename.endswith('xlsx'):
            self.filetype = 'excel'
        elif filename.endswith('.csv'):
            self.filetype = 'csv'

    def read(self):
        if self.filetype == 'excel':
            self._read_excel()
        elif self.filetype == 'csv':
            self._read_csv()

    def _read_excel(self):
        self.df = pandas.read_excel(self.filename)

    def _read_csv(self):
        self.df = pandas.read_csv(self.filename)
        self.df.rename(columns=lambda x: x.strip(), inplace=True)

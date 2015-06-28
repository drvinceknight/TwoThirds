"""A module for the data import handler"""

class Data:
    def __init__(self, filename):
        self.filename = filename
        if filename.endswith('.xls') or filename.endswith('xlsx'):
            self.filetype = 'excel'
        elif filename.endswith('.csv'):
            self.filetype = 'csv'

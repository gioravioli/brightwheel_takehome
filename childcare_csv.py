from utils import clean_fields
import pandas as pd


class ChildcareCSV():
    def __init__(self, db, filename):
        self.db = db
        self.filename = filename

    def add_all(self):
        names = ['name', 'type', 'address', 'city', 'state', 'zip', 'phone']
        df = pd.read_csv(self.filename, names=names).fillna('').astype(str)
        for i, row in df.iterrows():
            fields = clean_fields(row.to_dict())
            self.db.add_provider(fields=fields)
        return self

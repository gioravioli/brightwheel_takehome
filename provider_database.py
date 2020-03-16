from constants import FIELD_NAMES, DB_NAME, TABLE_NAME
import sqlite3


class ProviderDatabase():
    def __init__(self, memory=False):
        self.conn = sqlite3.connect(":memory:" if memory else DB_NAME)
        self.cursor = self.conn.cursor()
        columns = ', '.join(f"{field} VARCHAR" for field in FIELD_NAMES)
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ({columns});")

    def _get_conditions(self, fields):
        return ' AND '.join(
            f"({k}=\"{v}\" OR {k} IS NULL)" for k, v in fields.items())

    def provider_exists(self, fields):
        c = self.cursor
        where = self._get_conditions(fields)
        c.execute(f"SELECT * FROM {TABLE_NAME} WHERE {where}")
        return c.fetchone() is not None

    def add_provider(self, fields):
        c = self.cursor
        if self.provider_exists(fields):
            set = ', '.join(f"{k}=\"{v}\"" for k, v in fields.items())
            where = self._get_conditions(fields)
            c.execute(f"UPDATE {TABLE_NAME} SET {set} WHERE {where}")
        else:
            col_names = ','.join(fields.keys())
            values = ','.join(f"\"{x}\"" for x in fields.values())
            c.execute(
                f"INSERT INTO {TABLE_NAME} ({col_names}) VALUES({values});")

    def get_all_sorted(self):
        c = self.cursor
        c.execute(f"SELECT * FROM {TABLE_NAME} ORDER BY 1, 2, 3")
        return c.fetchall()

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()

    def __repr__(self):
        return '\n'.join(', '.join(x for x in r)
                         for r in self.get_all_sorted())

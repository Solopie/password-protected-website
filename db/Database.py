import sqlite3 as sql
import logging

class Database:
    def __init__(self, path):
        # I don't know if I'm doing the logging right :)
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.path = path

    def query(self,query, params=(), commit=False):
        rows = []
        try:
            with sql.connect(self.path) as con:
                con.row_factory = sql.Row
                cur = con.cursor()
                cur.execute(query, params)

                # If we're running insert or update we commit and don't return anything
                if commit:
                    con.commit()
                else:
                    rows = cur.fetchall()
            con.close()
        except Exception as e:
            self.logger.exception(e)

        return rows

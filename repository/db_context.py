from contextlib import closing
import sqlite3


class DbContext(object):
    @classmethod
    def get_connection(cls, database_path):
        return sqlite3.connect(database_path, detect_types=sqlite3.PARSE_DECLTYPES)

    @classmethod
    def rebuild_database(cls, connection, open_fn):
        with closing(connection) as db:
            with open_fn('schema/schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()
        return 'Database was rebuilt'


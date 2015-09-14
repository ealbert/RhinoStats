import os
from repository.db_context import DbContext


class DatabaseUtils(object):

    @classmethod
    def _get_database_test_path(cls):
        dir_path = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
        db_path = os.path.join(dir_path, 'test_database.db')
        return db_path

    @classmethod
    def _open_schema_file(cls, resource, mode='rb'):
        if mode not in ('r', 'rb'):
            raise ValueError('Resources can only be opened for reading')
        file_path = os.path.realpath(os.path.realpath(__file__) + '/../../../schema/schema.sql')
        return open(file_path, mode)

    @classmethod
    def recreate_database(cls, connection):
        return DbContext.rebuild_database(connection, cls._open_schema_file)

    @classmethod
    def get_db_connection(cls):
        db_path = DatabaseUtils._get_database_test_path()
        return DbContext.get_connection(db_path)

    @classmethod
    def get_db_connection_in_memory(cls):
        return DbContext.get_connection(':memory:')


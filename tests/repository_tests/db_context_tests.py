import unittest

from tests.database.database_utils import DatabaseUtils

__author__ = 'eagleiser'


class DbContextTests(unittest.TestCase):

    def test_create_schema_in_memory(self):
        msg = DatabaseUtils.recreate_database(DatabaseUtils.get_db_connection_in_memory())
        expected = 'Database was rebuilt'
        self.assertEqual(expected, msg)

    def test_create_schema(self):
        msg = DatabaseUtils.recreate_database(DatabaseUtils.get_db_connection())
        expected = 'Database was rebuilt'
        self.assertEqual(expected, msg)

if __name__ == '__main__':
    unittest.main()

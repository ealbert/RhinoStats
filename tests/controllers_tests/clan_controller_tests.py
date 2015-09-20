import datetime
from controllers.clan_controller import ClanController
from tests.common.TestTime import TestTime
from tests.database.database_utils import DatabaseUtils
from tests.fixtures.account_stats_fixtures import AccountStatsFixtures
from repository.player_repository import PlayerRepository
from utils.app_time import AppTime

__author__ = 'eagleiser'

import unittest


class ClanControllerTests(unittest.TestCase):

    def test_player_does_not_require_calculation(self):
        TestTime.set_app_time(datetime.datetime(2015, 8, 1, 12, 0, 0))
        player_data = {'last_update': AppTime.get_now()}
        controller = ClanController()
        result = controller.requires_recalculation( player_data)
        expected = False
        self.assertEqual(expected, result)

    def test_player_requires_calculation(self):
        TestTime.set_app_time(datetime.datetime(2015, 8, 1))
        player_data = {'last_update': datetime.datetime(2015, 7, 31)}
        controller = ClanController()
        result = controller.requires_recalculation(player_data)
        expected = True
        self.assertEqual(expected, result)

    def test_get_player_data_that_is_not_in_database(self):
        TestTime.set_app_time(datetime.datetime(2015, 8, 1))
        conn = DatabaseUtils.get_db_connection()
        DatabaseUtils.recreate_database(conn)
        conn = DatabaseUtils.get_db_connection()
        controller = ClanController()
        controller._retrieve_account_stats = lambda account_id, app_id: AccountStatsFixtures.standard_accounts_record()
        player_data = controller.get_player_data(conn, 'app_id', 500050913, 512841364, 'test_player')
        expected = {
            "clan_id": 500050913,
            "account_id": 512841364,
            "account_name": 'test_player',
            "total_resources_earned": 5002,
            "stronghold_defense_battles": 9,
            "thirty_day_defense_battles": 0,
            "stronghold_skirmish_battles": 731,
            "thirty_day_skirmish_battles": 0,
            "seven_day_resources_earned": 0,
            "thirty_day_resources_earned": 0,
            "last_update": AppTime.get_now()
        }
        self.assertEqual(expected, player_data)
        from_date = AppTime.get_now()
        to_date = from_date - datetime.timedelta(days=30)
        rows = PlayerRepository.get_player_stats(conn, player_data['clan_id'], player_data['account_id'], from_date, to_date)
        self.assertEqual(1, len(rows))
        player_stat_snapshot_dict = dict(zip(rows[0].keys(), rows[0]))
        expected = {'stronghold_defense_battles': 9,
                    'account_id': 512841364,
                    'stronghold_skirmish_battles': 731,
                    'clan_id': 500050913,
                    'total_resources_earned': 5002,
                    'created_date': str(AppTime.get_now())}
        self.assertEqual(expected, player_stat_snapshot_dict)

    def test_create_player_stat(self):
        TestTime.set_app_time(datetime.datetime(2015, 8, 1))
        DatabaseUtils.recreate_database(DatabaseUtils.get_db_connection())
        conn = DatabaseUtils.get_db_connection()
        player_data = {'clan_id': 1,
                       'account_id': 777,
                       'account_name': 'test player',
                       'total_resources_earned': 1200,
                       'stronghold_skirmish_battles': 100,
                       'stronghold_defense_battles': 10,
                       'seven_day_resources_earned': 320,
                       'thirty_day_resources_earned': 320,
                       'last_update': AppTime.get_now(),
                       'thirty_day_defense_battles': 0,
                       'thirty_day_skirmish_battles': 0}
        controller = ClanController()
        controller.create_player_stat(conn, player_data)
        row = PlayerRepository.get_player(conn, player_data['clan_id'], player_data['account_id'])
        player_stat_dict = dict(zip(row.keys(), row))
        expected = {'clan_id': 1,
                    'account_id': 777,
                    'account_name': u'test player',
                    'total_resources_earned': 1200,
                    'stronghold_skirmish_battles': 100,
                    'thirty_day_skirmish_battles': 0,
                    'stronghold_defense_battles': 10,
                    'thirty_day_defense_battles': 0,
                    'seven_day_resources_earned': 320,
                    'thirty_day_resources_earned': 320,
                    'last_update': str(AppTime.get_now())}
        self.assertEqual(expected, player_stat_dict)
        from_date = AppTime.get_now()
        to_date = from_date - datetime.timedelta(days=30)
        rows = PlayerRepository.get_player_stats(conn, player_data['clan_id'], player_data['account_id'], from_date, to_date)
        self.assertEqual(1, len(rows))
        player_stat_snapshot_dict = dict(zip(rows[0].keys(), rows[0]))
        expected = {'stronghold_defense_battles': 10,
                    'account_id': 777,
                    'stronghold_skirmish_battles': 100,
                    'clan_id': 1,
                    'total_resources_earned': 1200,
                    'created_date': str(AppTime.get_now())}
        self.assertEqual(expected, player_stat_snapshot_dict)

if __name__ == '__main__':
    unittest.main()

import unittest
import datetime
from tests.common.TestTime import TestTime

from tests.fixtures.account_stats_fixtures import AccountStatsFixtures
from mappers.account_stats_to_player_data_mapper import AccountStatsToPlayerDataMapper
from utils.app_time import AppTime


class AccountStatsToPlayerDataMapperTests(unittest.TestCase):
    def test_empty_source_data(self):
        accounts_data = {}
        player_data = AccountStatsToPlayerDataMapper.map(accounts_data, 0, 'test_player')
        expected = {}
        self.assertEqual(expected, player_data)
        accounts_data = None
        player_data = AccountStatsToPlayerDataMapper.map(accounts_data, 0, 'test_player')
        self.assertEqual(expected, player_data)

    def test_normal_data(self):
        TestTime.set_app_time(datetime.datetime(2015, 8, 1))
        player_data = AccountStatsToPlayerDataMapper.map(AccountStatsFixtures.standard_accounts_record(),
                                                         512841364, 'test_player')
        expected = {
            "clan_id": 500050913,
            "account_id": 512841364,
            "account_name": 'test_player',
            "total_resources_earned": 5002,
            "stronghold_defense_battles": 9,
            "stronghold_skirmish_battles": 731,
            "seven_day_resources_earned": 0,
            "thirty_day_resources_earned": 0,
            "last_update": AppTime.get_now()
        }
        self.assertEqual(expected, player_data)


if __name__ == '__main__':
    unittest.main()

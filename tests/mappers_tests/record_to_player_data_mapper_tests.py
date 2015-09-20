import unittest
import datetime
from mappers.record_to_player_data_mapper import RecordToPlayerDataMapper
from tests.common.TestTime import TestTime

from tests.fixtures.account_stats_fixtures import AccountStatsFixtures
from mappers.account_stats_to_player_data_mapper import AccountStatsToPlayerDataMapper
from utils.app_time import AppTime


class RecordToPlayerDataMapperTests(unittest.TestCase):
    def test_map(self):
        now = AppTime.get_now()
        record = {"clan_id": 500050913,
            "account_id": 512841364,
            "account_name": 'test_player',
            "total_resources_earned": 5002,
            "stronghold_defense_battles": 9,
            "thirty_day_defense_battles": 0,
            "stronghold_skirmish_battles": 731,
            "thirty_day_skirmish_battles": 0,
            "seven_day_resources_earned": 0,
            "thirty_day_resources_earned": 0,
            "last_update": now
        }
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
            "last_update": now
        }
        result = RecordToPlayerDataMapper.map(record)
        self.assertEqual(expected, result)
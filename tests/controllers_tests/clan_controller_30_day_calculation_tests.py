from asyncio.test_utils import TestCase
import datetime

from controllers.clan_controller import ClanController
from tests.common.TestTime import TestTime
from tests.database.database_utils import DatabaseUtils
from tests.fixtures.account_stats_fixtures import AccountStatsFixtures
from utils.app_time import AppTime

__author__ = 'enrique'

import unittest


class ClanController30DayTests(unittest.TestCase):

    def test_one_month_of_updates(self):
        """"
            Adds stats for a month
            Starts with:
            "total_resources_earned": 5002
            "week_resources_earned": 0
            "battles": 731

            It should end up with:
            "total_resources_earned": 5002 + 65 = 5067
            "week_resources_earned": 20
            30 day = 65
        """""
        TestTime.set_app_time(datetime.datetime(2015, 8, 1))
        account_stats = AccountStatsFixtures.standard_accounts_record()
        player_stats = AccountStatsFixtures.personal_data_response()
        conn = DatabaseUtils.get_db_connection()
        DatabaseUtils.recreate_database(conn)
        conn = DatabaseUtils.get_db_connection()
        controller = ClanController()
        controller._retrieve_account_stats = lambda account_id, app_id: account_stats
        controller._retrieve_personal_stats = lambda account_id, app_id: player_stats
        members = [{'account_id': 512841364, 'account_name': 'test_player'}]
        players_data = controller.get_players_data(conn, 123, 123, members)
        self.assertEqual(1, len(players_data))
        TestTime.set_app_time(datetime.datetime(2015, 8, 5))
        self._amend_accounts_stats(account_stats, 10, 1, 10)
        controller.get_players_data(conn, 123, 500050913, members)
        TestTime.set_app_time(datetime.datetime(2015, 8, 10))
        self._amend_accounts_stats(account_stats, 35, 2, 45)
        controller.get_players_data(conn, 123, 500050913, members)
        TestTime.set_app_time(datetime.datetime(2015, 8, 15))
        self._amend_accounts_stats(account_stats, 0, 2, 35)
        controller.get_players_data(conn, 123, 500050913, members)
        TestTime.set_app_time(datetime.datetime(2015, 8, 25))
        self._amend_accounts_stats(account_stats, 20, 1, 20, 10)
        self._amend_player_stats(player_stats, 21, 10)
        controller.get_players_data(conn, 123, 500050913, members)
        TestTime.set_app_time(datetime.datetime(2015, 8, 31))
        players_data = controller.get_players_data(conn, 123, 500050913, members)
        expected = {
            "clan_id": 500050913,
            "account_id": 512841364,
            "account_name": 'test_player',
            'all_battles':25367,
            'clan_battles': 46,
            "total_resources_earned": 5067,
            "stronghold_defense_battles": 19,
            "thirty_day_defense_battles": 10,
            "stronghold_skirmish_battles": 737,
            "thirty_day_skirmish_battles": 6,
            "seven_day_resources_earned": 20,
            "thirty_day_resources_earned": 65,
            'thirty_day_clan_battles': 0,
            'thirty_day_all_battles': 21,
            "last_update": AppTime.get_now()
        }
        self.maxDiff = None
        self.assertEqual(expected, players_data[0])

    def _amend_accounts_stats(self, account_stats, additional_resources, skirmish_battles, week_resources, defense_battles=0):
        account_stats['data']['512841364']['total_resources_earned'] += additional_resources
        account_stats['data']['512841364']['stronghold_skirmish']['battles'] += skirmish_battles
        account_stats['data']['512841364']['week_resources_earned'] = week_resources
        account_stats['data']['512841364']['stronghold_defense']['battles'] += defense_battles

    def _amend_player_stats(self, player_stats, all_battles, clan_battles):
        player_stats['data']['512841364']['statistics']['all']['battles'] += all_battles
        player_stats['data']['512841364']['statistics']['clan']['battles'] += clan_battles


if __name__ == '__main__':
    unittest.main()

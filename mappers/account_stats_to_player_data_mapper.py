from utils.app_time import AppTime

__author__ = 'eagleiser'
class AccountStatsToPlayerDataMapper(object):

    @classmethod
    def map(cls, accounts_stats, account_id, account_name):
        player_data = {}
        if accounts_stats is None or not accounts_stats:
            return player_data
        data = accounts_stats['data'][str(account_id)]
        player_data = {
            "clan_id": data['clan_id'],
            "account_id": data['account_id'],
            "account_name": account_name,
            "total_resources_earned": data['total_resources_earned'],
            "stronghold_defense_battles": data['stronghold_defense']['battles'] if data['stronghold_defense'] else 0,
            "thirty_day_defense_battles": 0,
            "stronghold_skirmish_battles": data['stronghold_skirmish']['battles'] if data['stronghold_skirmish'] else 0,
            "thirty_day_skirmish_battles": 0,
            "seven_day_resources_earned": data['week_resources_earned'],
            "thirty_day_resources_earned": data['week_resources_earned'],
            "last_update": AppTime.get_now()
        }
        return player_data

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

    @classmethod
    def amend_player_data(cls, player_data, personal_stats, account_id):
        data = personal_stats['data'][str(account_id)]['statistics']
        clan_battles = data['globalmap_absolute']['battles'] if data['globalmap_absolute'] else 0
        clan_battles += data['globalmap_middle']['battles'] if data['globalmap_middle'] else 0
        clan_battles += data['globalmap_champion']['battles'] if data['globalmap_middle'] else 0
        player_data['clan_battles'] = clan_battles
        player_data['thirty_day_clan_battles'] = 0
        player_data['all_battles'] = data['all']['battles'] if data['all'] else 0
        player_data['thirty_day_all_battles'] = 0
        return player_data

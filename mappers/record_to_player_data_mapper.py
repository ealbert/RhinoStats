__author__ = 'enrique'


class RecordToPlayerDataMapper(object):

    @classmethod
    def map(cls, record):
        player_data = {}
        if record is None or not record:
            return player_data
        player_data = {
            "clan_id": record['clan_id'],
            "account_id": record['account_id'],
            "account_name": record['account_name'],
            "total_resources_earned": record['total_resources_earned'],
            "stronghold_defense_battles": record['stronghold_defense_battles'],
            "thirty_day_defense_battles": record['thirty_day_defense_battles'],
            "stronghold_skirmish_battles": record['stronghold_skirmish_battles'],
            "thirty_day_skirmish_battles": record['thirty_day_skirmish_battles'],
            "seven_day_resources_earned": record['seven_day_resources_earned'],
            "thirty_day_resources_earned": record['thirty_day_resources_earned'],
            "clan_battles": record['clan_battles'],
            "thirty_day_clan_battles": record['thirty_day_clan_battles'],
            "all_battles": record['all_battles'],
            "thirty_day_all_battles": record['thirty_day_all_battles'],
            "last_update": record['last_update']
        }
        return player_data

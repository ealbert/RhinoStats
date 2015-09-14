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
            "stronghold_skirmish_battles": record['stronghold_skirmish_battles'],
            "seven_day_resources_earned": record['seven_day_resources_earned'],
            "thirty_day_resources_earned": record['thirty_day_resources_earned'],
            "last_update": record['last_update']
        }
        return player_data

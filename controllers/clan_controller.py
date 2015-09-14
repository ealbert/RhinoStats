import datetime
from mappers.record_to_player_data_mapper import RecordToPlayerDataMapper
from repository.player_repository import PlayerRepository
from utils.app_time import AppTime
from utils.request_utils import RequestUtils
from mappers.account_stats_to_player_data_mapper import AccountStatsToPlayerDataMapper


class ClanController(object):
    def get_clan_stats(self, connection, clan_id):
        app_id = '2a138f1eafc3834fe2c3eecbd71ee762'
        members = self.get_clan_members(connection, clan_id, app_id)
        players_data = self.get_players_data(connection, app_id, clan_id, members)
        return players_data

    def get_clan_members(self, connection, clan_id, app_id):
        url = 'http://api.worldoftanks.eu/wgn/clans/info/?application_id={app_id}&clan_id={clan_id}'\
            .format(app_id=app_id, clan_id=clan_id)
        data = RequestUtils.retrieve_json(url)
        clan_data = data['data'][clan_id]
        members = clan_data['members']
        return members

    def get_players_data(self, connection, app_id, clan_id, members):
        players_data = []
        for member in members:
            account_id = member['account_id']
            account_name = member['account_name']
            try:
                player_data = self.get_player_data(connection, app_id, clan_id, account_id, account_name)
                if self.requires_recalculation(player_data):
                    # get accounts stat
                    account_stats = self._retrieve_account_stats(account_id, app_id)
                    player_data = AccountStatsToPlayerDataMapper.map(account_stats, account_id, account_name)
                    # create snapshot
                    self.create_snapshot(connection, player_data)
                    # calculate 30 day
                    from_date = AppTime.get_now() - datetime.timedelta(days=30)
                    total_resources_earned = PlayerRepository.get_total_resources_at_date(connection, player_data['clan_id'],
                                                                                          player_data['account_id'],
                                                                                          from_date)
                    player_data['thirty_day_resources_earned'] = player_data['total_resources_earned'] - total_resources_earned
                    # update player_stat
                    PlayerRepository.update_player_stats(connection, player_data)
                players_data.append(player_data)
            except Exception as e:
                print('Failed on player: {account_name} - error: {error}'
                      .format(account_name=member['account_name'], error=str(e)))
        players_data.sort(key=lambda x: x['account_name'].lower())
        return players_data

    def get_player_data(self, connection, app_id, clan_id, account_id, account_name):
        record = PlayerRepository.get_player(connection, clan_id, account_id)
        if record is None:
            account_stats = self._retrieve_account_stats(account_id, app_id)
            player_data = AccountStatsToPlayerDataMapper.map(account_stats, account_id, account_name)
            self.create_player_stat(connection, player_data)
        else:
            player_data = RecordToPlayerDataMapper.map(record)
        return player_data

    def _retrieve_account_stats(self, account_id, app_id):
        url = 'http://api.worldoftanks.eu/wot/stronghold/accountstats/?application_id={app_id}&account_id={account_id}'\
            .format(app_id=app_id, account_id=account_id)
        return RequestUtils.retrieve_json(url)

    def create_player_stat(self, connection, player_data):
        row = [player_data['clan_id'],
               player_data['account_id'],
               player_data['account_name'],
               player_data['total_resources_earned'],
               player_data['stronghold_defense_battles'],
               player_data['stronghold_skirmish_battles'],
               player_data['seven_day_resources_earned'],
               player_data['thirty_day_resources_earned'],
               player_data['last_update'],
               player_data['last_update']]
        PlayerRepository.create_player_stat(connection, row)
        self.create_snapshot(connection, player_data)

    def create_snapshot(self, connection, player_data):
        row = [player_data['clan_id'],
               player_data['account_id'],
               player_data['total_resources_earned'],
               player_data['stronghold_defense_battles'],
               player_data['stronghold_skirmish_battles'],
               player_data['last_update']]
        PlayerRepository.create_player_stat_snapshot(connection, row)

    def requires_recalculation(self, player_data):
        last_update = player_data['last_update'] \
            if isinstance(player_data['last_update'], datetime.datetime) \
            else datetime.datetime.strptime(player_data['last_update'], '%Y-%m-%d %H:%M:%S')
        diff_time = AppTime.get_now() - last_update
        max_delta_time = datetime.timedelta(days=1)
        if diff_time < max_delta_time:
            return False
        return True





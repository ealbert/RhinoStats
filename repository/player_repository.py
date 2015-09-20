from utils.app_time import AppTime

__author__ = 'eagleiser'
import sqlite3 as lite


class PlayerRepository(object):
    @classmethod
    def get_player(cls, connection, clan_id, account_id):
        sql = """
                SELECT
                    clan_id, account_id, account_name, total_resources_earned,
                    stronghold_defense_battles, thirty_day_defense_battles,
                    stronghold_skirmish_battles, thirty_day_skirmish_battles,
                    seven_day_resources_earned, thirty_day_resources_earned,
                    datetime(last_update) last_update
                FROM
                    player_stats
                WHERE
                    clan_id = ? AND
                    account_id = ?
              """
        with connection:
            connection.row_factory = lite.Row
            cur = connection.cursor()
            cur.execute(sql, [clan_id, account_id])
            row = cur.fetchone()
            return row

    @classmethod
    def get_stats_at_date(cls, connection, clan_id, account_id, from_date):
        sql = """
            SELECT total_resources_earned, stronghold_defense_battles, stronghold_skirmish_battles
              from player_stats_snapshot
              where
                created_date >= ? AND
                clan_id = ? AND
                account_id = ?
              order by created_date asc LIMIT 1
        """
        with connection:
            connection.row_factory = lite.Row
            cur = connection.cursor()
            cur.execute(sql, [from_date, clan_id, account_id])
            row = cur.fetchone()
            if row is None:
                return 0
            return row['total_resources_earned'], \
                   row['stronghold_defense_battles'], \
                   row['stronghold_skirmish_battles']

    @classmethod
    def get_player_stats(cls, connection, clan_id, account_id, from_date, to_date):
        sql = """
                SELECT
                    clan_id, account_id, total_resources_earned, stronghold_defense_battles,
                    stronghold_skirmish_battles, datetime(created_date) created_date
                FROM
                    player_stats_snapshot
                WHERE
                    clan_id = ? AND
                    account_id = ? AND
                    created_date Between ? and ?
              """
        with connection:
            connection.row_factory = lite.Row
            cur = connection.cursor()
            cur.execute(sql, [clan_id, account_id, to_date, from_date])
            rows = cur.fetchall()
            return rows

    @classmethod
    def update_player_stats(cls, connection, player_data):
        sql = """
            UPDATE player_stats SET
                total_resources_earned = ?,
                stronghold_defense_battles = ?,
                stronghold_skirmish_battles = ?,
                seven_day_resources_earned = ?,
                thirty_day_resources_earned = ?,
                thirty_day_defense_battles = ?,
                thirty_day_skirmish_battles = ?,
                last_update = ?
            WHERE
                clan_id = ? AND
                account_id = ?
        """
        values = [
            player_data['total_resources_earned'],
            player_data['stronghold_defense_battles'],
            player_data['stronghold_skirmish_battles'],
            player_data['seven_day_resources_earned'],
            player_data['thirty_day_resources_earned'],
            player_data['thirty_day_defense_battles'],
            player_data['thirty_day_skirmish_battles'],
            AppTime.get_now(),
            player_data['clan_id'],
            player_data['account_id']
        ]
        with connection:
            cur = connection.cursor()
            cur.execute(sql, values)

    @classmethod
    def create_player_stat(cls, connection, row):
        sql = """
              INSERT INTO player_stats
                 (clan_id, account_id, account_name, total_resources_earned,
                 stronghold_defense_battles, thirty_day_defense_battles,
                    stronghold_skirmish_battles, thirty_day_skirmish_battles,
                    seven_day_resources_earned, thirty_day_resources_earned,
                    created_date, last_update)
              VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
              """
        with connection:
            cur = connection.cursor()
            cur.execute(sql, row)

    @classmethod
    def create_player_stat_snapshot(cls, connection, row):
        sql = """
              INSERT INTO player_stats_snapshot
                 (clan_id, account_id, total_resources_earned, stronghold_defense_battles,
                    stronghold_skirmish_battles, created_date)
              VALUES(?, ?, ?, ?, ?, ?)
              """
        with connection:
            cur = connection.cursor()
            cur.execute(sql, row)

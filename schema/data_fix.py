import rhino_stats
import sqlite3 as lite

__author__ = 'enrique'


class DataFix(object):

    @classmethod
    def update_clan_and_all(cls):
        return  # do nothing !!!
        connection = rhino_stats.connect_db()
        sql = """
        select account_id, min(created_date) as created_date from player_stats_snapshot WHERE all_battles != 0 GROUP BY account_id
        """

        with connection:
            connection.row_factory = lite.Row
            cur = connection.cursor()
            cur.execute(sql)
            rows = cur.fetchall()

        sql = """
        select clan_battles, all_battles from player_stats_snapshot WHERE account_id = {account_id}
        and created_date = '{created_date}'
        """
        members = {}
        for row_account in rows:
            with connection:
                connection.row_factory = lite.Row
                cur = connection.cursor()
                script = sql.format(account_id=row_account['account_id'], created_date=row_account['created_date'])
                cur.execute(script)
                row = cur.fetchone()
                members[row_account['account_id']] = {'clan_battles': row['clan_battles'],
                                                      'all_battles': row['all_battles']}

        sql = """
        update player_stats_snapshot set clan_battles = {clan_battles}, all_battles =  {all_battles}
        WHERE account_id ={account_id} and all_battles = 0
        """

        for account_id in members:
            data = members[account_id]
            with connection:
                cur = connection.cursor()
                cur.execute(sql.format(account_id=account_id, clan_battles=data['clan_battles'],
                                       all_battles=data['all_battles']))


if __name__ == '__main__':
    DataFix.update_clan_and_all()

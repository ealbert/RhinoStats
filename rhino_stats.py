import os

from flask import Flask, render_template
from controllers.clan_controller import ClanController
from repository.db_context import DbContext
from utils.rating_calculator import RatingCalculator

DATABASE = 'wot_fortaleza.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = '12345'

app = Flask(__name__)
app.config.from_object(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top


@app.route('/')
def hello_world():
    clan_id = '500050913' # This is PU clan id
    players_data = ClanController().get_clan_stats(connect_db(), clan_id)
    enhanced_players_data = RatingCalculator.enhance_data(players_data)
    return render_template('player_stats.html', players_data=enhanced_players_data, clan_id=clan_id)


@app.route('/rebuild_db')
def rebuild_db():
    try:
        connection = connect_db()
        msg = DbContext.rebuild_database(connection, app.open_resource)
    except Exception as e:
        msg = 'Rebuilding the database an exception took place: %s' % str(e)
    return msg


def connect_db():
    database_path = os.path.join(APP_ROOT, 'database/' + app.config['DATABASE'])
    return DbContext.get_connection(database_path)


if __name__ == '__main__':
    app.run('0.0.0.0')

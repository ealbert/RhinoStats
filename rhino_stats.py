import csv
from io import StringIO
import os

from flask import Flask, render_template, make_response, request
from controllers.clan_controller import ClanController
from repository.db_context import DbContext
from utils.csv_exporter import CsvExporter, excel_semicolon
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
def home():
    return render_template('home.html', context='')


@app.route('/search_clan', methods=['POST'])
def search_clan():
    clan_name = request.form['search']
    controller = ClanController()
    search_details = controller.find_clan(clan_name)
    if search_details:
        if len(search_details) > 1:
            msg = '{clans} clans were found - please select one from bellow'.format(clans=str(len(search_details)))
            return render_template('home.html', context={'msg': msg, 'search_details': search_details,
                                                         'clan_name': clan_name})
        else:
            return _clan_stats(search_details[0]['clan_id'])
    else:
        msg = 'Clan was not found with that name or/and tag'
        return render_template('home.html', context={'msg': msg, 'search_details': [], 'clan_name': clan_name})

@app.route('/clan_stats/<clan_id>')
def _clan_stats(clan_id):
    players_data, clan_details = ClanController().get_clan_stats(connect_db(), clan_id)
    enhanced_players_data = RatingCalculator.enhance_data(players_data)
    return render_template('player_stats.html', players_data=enhanced_players_data, clan_details=clan_details)


@app.route('/csv/<clan_id>')
def clan_stats_csv(clan_id):
    players_data, _ = ClanController().get_clan_stats(connect_db(), clan_id)
    data = CsvExporter.get_data_into_list(players_data)
    si = StringIO()
    cw = csv.writer(si, dialect=excel_semicolon)
    cw.writerows(data)
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=rhino_stats.csv"
    output.headers["Content-type"] = "text/csv"
    return output


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

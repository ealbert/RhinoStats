from utils.app_time import AppTime

__author__ = 'eagleiser'


class TestTime(object):
    @classmethod
    def set_app_time(cls, app_datetime):
        AppTime.get_now = classmethod(lambda x: app_datetime)

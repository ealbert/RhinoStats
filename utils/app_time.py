import datetime

__author__ = 'eagleiser'
class AppTime(object):

    @classmethod
    def get_now(cls):
        return datetime.datetime.now()

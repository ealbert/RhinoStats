import json
import urllib


class RequestUtils(object):

    @classmethod
    def retrieve_json(cls, url):
        response = urllib.request.urlopen(url)
        str_response = response.read().decode('utf-8')
        return json.loads(str_response)

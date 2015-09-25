__author__ = 'enrique'


class CsvExporter(object):

    @classmethod
    def get_data_into_list(cls, data):
        output = []
        headers = list(data[0].keys())
        output.append(headers)
        for player in data:
            output.append(list(player.values()))
        return output

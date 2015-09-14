__author__ = 'enrique'


class RatingCalculator(object):
    @classmethod
    def enhance_data(cls, players_data):
        calculator = RatingCalculator()
        return calculator.add_all_rates(players_data)

    def add_all_rates(self, players_data):
        rates = [('total_resources_earned', 999),
                 ('seven_day_resources_earned', 49),
                 ('thirty_day_resources_earned', 199)]
        for rate in rates:
            self.add_rate(rate[0], rate[1], players_data)
        return players_data

    def add_rate(self, field_name, min_value, players_data):
        value_to_rate_map = [(0, 1), (min_value, 2)]
        max_value = max([x[field_name] for x in players_data])
        values = range(min_value+1, max_value, int(max_value / 7))
        rates = range(3, 10)
        value_to_rate_map.extend(zip(values, rates))
        for player_data in players_data:
            rate = self.get_rate(player_data[field_name], value_to_rate_map)
            player_data[field_name + '_rate'] = 's' + str(rate)

    def get_rate(self, value, value_to_rate_map):
        if value < 0:
            return 1
        for rate in value_to_rate_map:
            if rate[0] >= value:
                return rate[1]
        return 9

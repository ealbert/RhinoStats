from utils.rating_calculator import RatingCalculator

__author__ = 'enrique'

import unittest


class RatingCalculatorTests(unittest.TestCase):
    def test_total_resources(self):
        calculator = RatingCalculator()
        players_data = self.players_data()
        calculator.add_rate('total_resources_earned', 999, players_data)
        expected = [
            {'total_resources_earned': 16000,
             'seven_day_resources_earned': 320,
             'thirty_day_resources_earned': 320,
             'total_resources_earned_rate': 's9'},
            {'total_resources_earned': 1000,
             'seven_day_resources_earned': 150,
             'thirty_day_resources_earned': 200,
             'total_resources_earned_rate': 's3'},
            {'total_resources_earned': 900,
             'seven_day_resources_earned': 50,
             'thirty_day_resources_earned': 160,
             'total_resources_earned_rate': 's2'},
            {'total_resources_earned': 500,
             'seven_day_resources_earned': 30,
             'thirty_day_resources_earned': 30,
             'total_resources_earned_rate': 's2'},
            {'total_resources_earned': 0,
             'seven_day_resources_earned': 0,
             'thirty_day_resources_earned': 0,
             'total_resources_earned_rate': 's1'}
        ]
        self.maxDiff = None
        self.assertEqual(expected, players_data)

    def test_all_rates(self):
        players_data = self.players_data()
        result = RatingCalculator.enhance_data(players_data)
        first_player = result[0]
        expected = {'total_resources_earned': 16000,
                    'seven_day_resources_earned': 320,
                    'thirty_day_resources_earned': 320,
                    'total_resources_earned_rate': 's9',
                    'seven_day_resources_earned_rate': 's9',
                    'thirty_day_resources_earned_rate': 's9'}
        self.assertEqual(expected, first_player)
        second_player = result[1]
        expected = {'total_resources_earned': 1000,
                    'seven_day_resources_earned': 150,
                    'thirty_day_resources_earned': 200,
                    'total_resources_earned_rate': 's3',
                    'seven_day_resources_earned_rate': 's6',
                    'thirty_day_resources_earned_rate': 's3'}
        self.assertEqual(expected, second_player)
        fourth_player = result[3]
        expected = {'total_resources_earned': 500,
                    'seven_day_resources_earned': 30,
                    'thirty_day_resources_earned': 30,
                    'total_resources_earned_rate': 's2',
                    'seven_day_resources_earned_rate': 's2',
                    'thirty_day_resources_earned_rate': 's2'}
        self.assertEqual(expected, fourth_player)

    def players_data(self):
        return [
            {'total_resources_earned': 16000,
             'seven_day_resources_earned': 320,
             'thirty_day_resources_earned': 320},
            {'total_resources_earned': 1000,
             'seven_day_resources_earned': 150,
             'thirty_day_resources_earned': 200},
            {'total_resources_earned': 900,
             'seven_day_resources_earned': 50,
             'thirty_day_resources_earned': 160},
            {'total_resources_earned': 500,
             'seven_day_resources_earned': 30,
             'thirty_day_resources_earned': 30},
            {'total_resources_earned': 0,
             'seven_day_resources_earned': 0,
             'thirty_day_resources_earned': 0}
        ]


if __name__ == '__main__':
    unittest.main()

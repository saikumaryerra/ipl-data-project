import unittest

from best_entertainer_for_season import best_entertainer_for_season


class TestBestEntertainerForSeason(unittest.TestCase):
    def test_best_entertainer_for_season(self):
        inputs_and_outputs = [
            (
                ('./ipl/test_matches.csv','./ipl/test_deliveries.csv','2015'),
                ([53, 28, 24, 19],
                {'MI': 13, 'RPS': 7, 'RCB': 8, 'SRH': 4},
                {'MI': 2, 'RPS': 1, 'RCB': 0, 'SRH': 1},
                ['MI', 'RPS', 'RCB', 'SRH'],'Mumbai Indians'
                )
            ),
            (
                ('./ipl/test_matches.csv','./ipl/test_deliveries.csv','2016'),
                ([31, 53, 69, 56],
                {'GL': 8, 'KXP': 13, 'KKR': 16, 'RPS': 14},
                {'GL': 1, 'KXP': 2, 'KKR': 3, 'RPS': 2},
                ['GL', 'KXP', 'KKR', 'RPS'],
                'Kolkata Knight Riders'
                )
            )
        ]
        for args, expected_output in inputs_and_outputs:
            output=best_entertainer_for_season(*args)
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

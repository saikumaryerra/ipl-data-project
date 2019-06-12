import unittest

from best_entertainer import best_entertainer


class TestBestEntertainer(unittest.TestCase):
    def test_best_entertainer(self):
        inputs_and_outputs = [
            (
                ('./ipl/test_matches.csv','./ipl/test_deliveries.csv'),
                ([38, 64, 82, 64, 58, 32, 22],
                {'GL': 8, 'KXP': 13, 'KKR': 16, 'MI': 13, 'RPS': 10, 'RCB': 8, 'SRH': 4},
                {'GL': 1, 'KXP': 2, 'KKR': 3, 'MI': 2, 'RPS': 3, 'RCB': 0, 'SRH': 1},
                ['GL', 'KXP', 'KKR', 'MI', 'RPS', 'RCB', 'SRH'],
                'Kolkata Knight Riders'
                )
            )
        ]
        for args, expected_output in inputs_and_outputs:
            output=best_entertainer(*args)
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

import unittest

from economical_bowlers import economical_bowlers


class TestEconomicalBowlers(unittest.TestCase):
    def test_economical_bowlers(self):
        inputs_and_outputs = [
            (
                ('./ipl/test_matches.csv','./ipl/test_deliveries.csv'),(['R Bhatia', 'MC Henriques', 'MC Henriques', 'TS Mills', 'TS Mills'],[4.5, 6.0, 6.0, 8.0, 8.0])
            )
        ]
        for args, expected_output in inputs_and_outputs:
            output=economical_bowlers(*args)
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

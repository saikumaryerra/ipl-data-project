import unittest

from economical_bowlers import economical_bowlers,economical_bowlers_from_database


class TestEconomicalBowlers(unittest.TestCase):
    def test_economical_bowlers(self):
        inputs_and_outputs = [
            (
                ('./ipl/test_matches.csv','./ipl/test_deliveries.csv'),{'R Bhatia': 4.5, 'MC Henriques': 6.0, 'HH Pandya': 6.0, 'TS Mills': 8.0, 'Rashid Khan': 8.0})
        ]
        for args, expected_output in inputs_and_outputs:
            output=economical_bowlers(*args)
            self.assertEqual(output, expected_output)
    
    def test_economical_bowlers_from_database(self):
        inputs_and_outputs = [
            (
                ('test_matches','test_deliveries'),{'R Bhatia': 4.5, 'MC Henriques': 6.0, 'HH Pandya': 6.0, 'TS Mills': 8.0, 'Rashid Khan': 8.0})
        ]
        for args, expected_output in inputs_and_outputs:
            output=economical_bowlers_from_database(*args)
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

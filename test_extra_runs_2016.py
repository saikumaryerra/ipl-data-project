import unittest

from extra_runs_2016 import extra_runs_2016,extra_runs_2016_from_database


class TestExtraRuns2016(unittest.TestCase):
    def test_extra_runs_2016(self):
        inputs_and_outputs = [
            (('./ipl/test_matches.csv','./ipl/test_deliveries.csv'),{'KKR': 5, 'GL': 0, 'KXP': 0, 'RPS': 0})
        ]
        for args, expected_output in inputs_and_outputs:
            output=extra_runs_2016(*args)
            self.assertEqual(output, expected_output)
    def test_extra_runs_2016_from_database(self):
        inputs_and_outputs = [
            (('test_matches','test_deliveries'),{'KKR': 5, 'GL': 0, 'KXP': 0, 'RPS': 0})
        ]
        for args, expected_output in inputs_and_outputs:
            output=extra_runs_2016_from_database(*args)
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

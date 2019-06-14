import unittest

from matches_won_per_year import matches_won_per_year,matches_won_per_year_from_database


class TestMatchesWonPerYear(unittest.TestCase):
    def test_matches_Won_per_year(self):
        inputs_and_outputs = [('./ipl/test_matches.csv',{'2015': {'Gujarat Lions': 0, 'Mumbai Indians': 0, 'Rising Pune Supergiants': 1, 'Sun Risers Hyderabad': 1}, '2016': {'Gujarat Lions': 0, 'Kings XI Punjab': 1, 'Kolkata Knight Riders': 1, 'Mumbai Indians': 0, 'Rising Pune Supergiants': 0, 'Sun Risers Hyderabad': 0}})]
        for inp, expected_output in inputs_and_outputs:
            output = matches_won_per_year(inp)
            self.assertEqual(output, expected_output)
    
    def test_matches_Won_per_year_from_database(self):
        inputs_and_outputs = [('test_matches',{'2015': {'Gujarat Lions': 0, 'Mumbai Indians': 0, 'Rising Pune Supergiants': 1, 'Sun Risers Hyderabad': 1}, '2016': {'Gujarat Lions': 0, 'Kings XI Punjab': 1, 'Kolkata Knight Riders': 1, 'Mumbai Indians': 0, 'Rising Pune Supergiants': 0, 'Sun Risers Hyderabad': 0}})]
        for inp, expected_output in inputs_and_outputs:
            output = matches_won_per_year_from_database(inp)
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
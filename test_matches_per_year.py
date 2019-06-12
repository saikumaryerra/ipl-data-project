import unittest

from matches_per_year import matches_per_year


class TestMatchesPerYear(unittest.TestCase):
    def test_matches_per_year(self):
        inputs_and_outputs = [('./ipl/test_matches.csv',{'2015': 2, '2016': 2})]
        for inp, expected_output in inputs_and_outputs:
            output = matches_per_year(inp)
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
import unittest
import utils
from unittest.mock import patch

import exo1_star_naming as exo1


class Exo1Test(unittest.TestCase):

    @patch('builtins.input', new=utils.input_mock)
    @patch('builtins.print')
    def test_input1(self, mock_print):
        # Input set 1
        utils.return_values = ["Jupiter",
                               "Terre",
                               ""]
        exo1.main()
        mock_print.assert_called_with("Code de mission: J6T4 \n")

    @patch('builtins.input', new=utils.input_mock)
    @patch('builtins.print')
    def test_input2(self, mock_print):
        # Input set 2
        utils.return_values = ["Lune",
                               "Terre",
                               "Soleil",
                               ""]
        exo1.main()
        mock_print.assert_called_with("Code de mission: L3T4S5 \n")

    @patch('builtins.input', new=utils.input_mock)
    @patch('builtins.print')
    def test_input3(self, mock_print):
        # Input set 3
        utils.return_values = ["Terre",
                               "Mars",
                               "Mercure",
                               ""]
        exo1.main()
        mock_print.assert_called_with("Code de mission: T4M3Me5 \n")

    @patch('builtins.input', new=utils.input_mock)
    @patch('builtins.print')
    def test_input4(self, mock_print):
        # Input set 4
        utils.return_values = ["Pluton",
                               "Mercure",
                               "Terre",
                               "Mars",
                               "Calisto",
                               ""]
        exo1.main()
        mock_print.assert_called_with("Code de mission: P5M6T4Ma2C6 \n")


if __name__ == '__main__':
    unittest.main()

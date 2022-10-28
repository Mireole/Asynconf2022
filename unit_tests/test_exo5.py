import unittest
from unittest.mock import patch

import utils
import exo5_meteorite_attack as exo5


class Exo5Test(unittest.TestCase):

    @patch('builtins.input', new=utils.input_mock)
    @patch('builtins.print')
    def test_input1(self, mock_print):
        utils.return_values = ["O___O_OO__OO__VO_O_O",
                               "__O___O_OOO_OO_____O",
                               "OO___O___OOO_OOOOO_O",
                               "__OO__X__OO_O___O__O",
                               "_OO___OO______O___OO",
                               ""]
        exo5.main()
        mock_print.assert_called_with("G4;H4;I4;I5;J5;K5;L5;M5;N5;N4;O4;P4;P5;Q5;R5;R4;S4;S3;S2;R2;Q2;P2;O2;O1")

    @patch('builtins.input', new=utils.input_mock)
    @patch('builtins.print')
    def test_input2(self, mock_print):
        utils.return_values = ["X___OO__O___O",
                               "__O__OOOO____",
                               "OO_O__OO__O__",
                               "_OO_O____OO_O",
                               "__O_O__O_OOVO",
                               ""]
        exo5.main()
        mock_print.assert_called_with("A1;B1;C1;D1;D2;E2;E3;F3;F4;G4;H4;I4;I3;J3;J2;K2;L2;L3;L4;L5")


if __name__ == '__main__':
    unittest.main()

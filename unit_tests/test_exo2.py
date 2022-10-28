import unittest
from unittest.mock import patch

import utils
import exo2_phantom_2064_mission as exo2


class Exo2Test(unittest.TestCase):

    @patch('builtins.input', new=utils.input_mock)
    @patch('builtins.print')
    def test_input1(self, mock_print):
        utils.return_values = ["name=Crystal;speed=20000km/h;price=400/km", "10"]
        exo2.main()
        mock_print.assert_called_with("Le prix du trajet est de 1920000000€")

    @patch('builtins.input', new=utils.input_mock)
    @patch('builtins.print')
    def test_input2(self, mock_print):
        utils.return_values = ["name=Atmos;speed=2045km/h;price=23/km", "2"]
        exo2.main()
        mock_print.assert_called_with("Le prix du trajet est de 2257680€")

    @patch('builtins.input', new=utils.input_mock)
    @patch('builtins.print')
    def test_input3(self, mock_print):
        utils.return_values = ["name=CircleBurn;speed=178547km/h;price=3612/km", "6"]
        exo2.main()
        mock_print.assert_called_with("Le prix du trajet est de 92867294016€")

    @patch('builtins.input', new=utils.input_mock)
    @patch('builtins.print')
    def test_input4(self, mock_print):
        utils.return_values = ["name=SpaceDestroyer;speed=98928423km/h;price=9294/km", "12"]
        exo2.main()
        mock_print.assert_called_with("Le prix du trajet est de 264798939848256€")


if __name__ == '__main__':
    unittest.main()

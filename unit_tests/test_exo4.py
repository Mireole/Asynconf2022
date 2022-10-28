import unittest
from unittest.mock import patch

import utils
import exo4_supernovae as exo4


class Exo4Test(unittest.TestCase):

    @patch('builtins.input', new=utils.input_mock)
    @patch('builtins.print')
    def test(self, mock_print):
        utils.return_values = [
            "WwogICAgewogICAgICAgICJuYW1lIjogIlNpbG9wcCIsCiAgICAgICAgInNpemUiOiAxNDkyNCwKICAgICAgICAiZGlzdGFuY2VUb1N0YXIiOiA5MDI0ODQ1MiwKICAgICAgICAibWFzcyI6IDE5NDUzMgogICAgfSwKICAgIHsKICAgICAgICAibmFtZSI6ICJBc3RyaW9uIiwKICAgICAgICAic2l6ZSI6IDE1MjAwMCwKICAgICAgICAiZGlzdGFuY2VUb1N0YXIiOiAxNDkzMDIsCiAgICAgICAgIm1hc3MiOiAyMTk0CiAgICB9LAogICAgewogICAgICAgICJuYW1lIjogIlZhbGVudXMiLAogICAgICAgICJzaXplIjogMjkwNDUwLAogICAgICAgICJkaXN0YW5jZVRvU3RhciI6IDIwOTQ4NTkzNDU1LAogICAgICAgICJtYXNzIjogMTk1MjkzCiAgICB9Cl0="]
        exo4.main()
        mock_print.assert_called_with("")


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch

import utils
import exo3_task_gestion as exo3


class Exo3Test(unittest.TestCase):

    @patch('builtins.input', new=utils.input_mock)
    @patch('builtins.print')
    def test_commandes(self, mock_print):
        utils.return_values = ["ajouter", "Réparer la ventilation",
                               "La ventilation a actuellement un disfonctionnement", "Administrateur",
                               "ajouter-compte", "Crewmate", "n", "n",
                               "ajouter", "Réparer le système de chauffage", "Ca caille ici !",
                               "Administrateur,Crewmate",
                               "connecter", "Crewmate",
                               "liste",
                               "compléter", "Réparer le système de chauffage",
                               "connecter", "Administrateur",
                               "liste",
                               "supprimer-compte", "Crewmate",
                               "retirer", "Réparer la ventilation",
                               "liste",
                               "vider",
                               "liste",
                               "quitter"]
        exo3.main()
        mock_print.assert_any_call("RIP Crewmate, à jamais dans nos coeurs")
        mock_print.assert_any_call("Vous n'avez aucune tâche. Profitez du répit !")
        mock_print.assert_any_call("Tâche ajoutée.")
        mock_print.assert_any_call("Tâche retirée.")
        mock_print.assert_any_call("Tâche complétée.")
        mock_print.assert_any_call("Tâches vidées.")
        mock_print.assert_any_call("Connecté en tant que Crewmate.")
        mock_print.assert_any_call("Compte ajouté.")


if __name__ == '__main__':
    unittest.main()

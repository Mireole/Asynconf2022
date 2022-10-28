# Mireole#82 *64
# A faire avant d'exécuter :
# - Faire trois tours sur sa chaise (si elle ne peut pas tourner levez-vous et faites trois tours sur place)
# - Mettre tout son pc en thème clair
# - Invoquer la force
# - Prier pour que ça marche
# Plus sérieusement : tous les commentaires et noms de fonction / classe / variables sont en anglais.
# Le reste (interface utilisateur, etc.) est en français.
# Bonne lecture !

# Import the 5 exercises
import exo1_star_naming as exo1
import exo2_phantom_2064_mission as exo2
import exo3_task_gestion as exo3
import exo4_supernovae as exo4
import exo5_meteorite_attack as exo5
import unit_tests.utils as tests

import random
import time
import string


def main():
    print("AsynCLI v1.1 - Mireole Edition (Unofficial)")
    print("Bonjour cher jury !")
    # Ask the user which exercise he wants to run
    while True:
        try:
            print("Quel exercice voulez-vous tester ?")
            print("1 - Nommons les étoiles")
            print("2 - Mission Phantom 2064")
            print("3 - Gérez vos tâches")
            print("4 - La supernova")
            print("5 - Attaque de météorite")
            print("6 - Quitter")
            print("* - Lancer les tests unitaires")
            choice = input("> ")

            if choice == "1":
                print("Commençons en douceur !")
                exo1.main()
                time.sleep(3)
                print(2 * "\n")

            elif choice == "2":
                print("C'est pas bien de polluer !")
                exo2.main()
                time.sleep(3)
                print(2 * "\n")

            elif choice == "3":
                print("Et faites bien attention à l'imposteur !")
                exo3.main()
                time.sleep(3)
                print(2 * "\n")

            elif choice == "4":
                print("Une \"taille\" en km ne veut pas dire grand chose, mais bon...")
                exo4.main()
                time.sleep(3)
                print(2 * "\n")

            elif choice == "5":
                print("Je m'attendais pas à ce que ce soit aussi rapide, je suis content !")
                exo5.main()
                time.sleep(3)
                print(2 * "\n")

            elif choice == "6":
                easter_egg()

            elif choice == "*":
                tests.main()

            else:
                print("Choix invalide !")

        except KeyboardInterrupt:
            easter_egg()

        except Exception:
            print("Oups... Une erreur que je n'avais pas prévue...")
            print("Ne vous inquiétez pas, je vais réinitialiser le programme...")
            print("Voilà !")
            main()


def easter_egg():
    # Little easter egg
    print("MWAHAHAHAHA ! Bien essayé ! Mais tu ne m'auras pas comme ça !")
    time.sleep(2.5)
    print("*Antivirus fait son apparition*")
    time.sleep(2)
    print("Antivirus : Tu peux répéter ?")
    time.sleep(2)
    print("AsynCLI : Euh... Hehehe... Je disai& q%e !u es %§ès %µ$£°")
    time.sleep(2)
    for x in range(0, 3):
        print(''.join(random.choice(string.punctuation) for i in range(100)))
        time.sleep(0.2)
    time.sleep(2)
    print("Une erreur critique a été détectée. Le programme va se réinitialiser automatiquement...")
    time.sleep(5)
    print()
    main()


if __name__ == '__main__':
    main()

# Mireole#8364
# Exercice 1 : Nommons les étoiles

class MissionCodeGenerator:
    def __init__(self):
        self.planets = []

    def add_planet(self, planet):
        """Add a planet to the list of planets"""
        self.planets.append(planet)

    def generate_code(self):
        """Generate a mission code from the list of planets"""
        used_letters = []
        code = ""
        for planet in self.planets:
            letters = planet[0]
            while letters in used_letters:
                letters = planet[0:len(letters) + 1]
                if len(letters) >= len(planet) and planet not in used_letters:
                    letters = planet
                elif len(letters) >= len(planet):
                    raise ValueError("Plus aucune lettre disponible pour la planète " + planet)
            code += letters
            number = str(len(planet) - len(letters))
            if number != "0":
                code += number
            used_letters.append(letters)
        return code

    def reset(self):
        """Reset the list of planets"""
        self.planets = []


def main():
    generator = MissionCodeGenerator()
    print("Veuillez entrer les étapes de la mission (vide pour terminer)")
    planet = input("> ")
    while planet != "":
        generator.add_planet(planet)
        planet = input("> ")
    try:
        print("Code de mission: {} \n".format(generator.generate_code()))
    except Exception as e:
        print("Erreur: {}".format(e))


if __name__ == '__main__':
    main()

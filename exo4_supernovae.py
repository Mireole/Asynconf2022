# Mireole#8364
# Exercice 4 : La supernova

import base64
import json
import binascii


class PlanetSorter:
    def __init__(self, planets):
        self.planets = planets

    def sort(self):
        """Sort the planets by their distance from the star."""
        # If the length of the list is 0 or 1, it is already sorted.
        if len(self.planets) <= 1:
            return self.planets
        # Initialize the list that will be sorted and the dictionary mapping the planet names to their distances.
        name_to_distance = {}
        distances = []
        for planet in self.planets:
            name_to_distance[planet["name"]] = planet["distanceToStar"]
            distances.append(planet["distanceToStar"])

        # My try at implementing insertion sort, using only its wikipedia page as a reference
        for i in range(1, len(distances)):
            j = i
            while j > 0 and distances[j] < distances[j - 1]:
                distances[j], distances[j - 1] = distances[j - 1], distances[j]
                j -= 1

        # Finalize the sort by mapping the distances to the planet names, in the right order
        sorted_planets = []
        for distance in distances:
            for planet in self.planets:
                if planet["distanceToStar"] == distance:
                    sorted_planets.append(planet)

        self.planets = sorted_planets

    def print_planets(self):
        """Print the planets in the required way."""
        print("Planètes du système :\n")
        for planet in self.planets:
            print("Nom : {}".format(planet["name"]))
            print("Taille : {}km".format(planet["size"]))
            print("Masse : {} tonnes".format(planet["mass"]))
            print("Distance à l'étoile : {}km".format(planet["distanceToStar"]))
            print("")


def main():
    secret_code = input("Entrez le code secret : ")
    try:
        planets = json.loads(base64.b64decode(secret_code))
    except binascii.Error:
        print("Code secret invalide, veuillez réessayer.")
        main()
        return
    planet_sorter = PlanetSorter(planets)
    planet_sorter.sort()
    planet_sorter.print_planets()  # EZ


if __name__ == "__main__":
    main()

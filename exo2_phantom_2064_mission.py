# Mireole#8364
# Exercice 2 : Mission Phantom 2064

PRICE_MULTIPLIER = 24


def to_dict(data):
    """Convert the flight data into a dictionary"""
    to_dic = {}
    entries = data.split(";")
    for entry in entries:
        split = entry.split("=")
        key = split[0]
        value = split[1]
        to_dic[key] = value
    return to_dic


def convert_data(data, time):
    """Convert the flight data dictionary into usable data"""
    new_data = {"name": data["name"], "speed": int(data["speed"].strip("km/h")),
                "price": int(data["price"].strip("/km")), "time": time}
    return new_data


def calculate_price(data):
    """Calculate the price of the flight"""
    return data["price"] * data["time"] * data["speed"] * PRICE_MULTIPLIER


def main():
    flight_data = input("Entrez les caractéristiques du vaisseau : ")
    success = False
    flight_time = 0
    while not success:
        try:
            flight_time = int(input("Entrez le temps de trajet : "))
        except ValueError:
            print("Erreur: le temps de trajet doit être un nombre entier, veuillez réessayer")
        else:
            success = True
    try:
        dic = convert_data(to_dict(flight_data), flight_time)
        price = calculate_price(dic)
    except Exception:
        print("Erreur: les données entrées sont invalides, veuillez réessayer")
        main()
        return
    print("Le prix du trajet est de {}€".format(price))


if __name__ == '__main__':
    main()

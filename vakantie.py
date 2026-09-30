def travel_costs(km: int) -> float:
    """
    Bepaalt de vervoerskosten op basis van de te rijden afstand
    naar de accomodatie (tel `km` twee keer voor heen en terug).
    """
    return 2*0.13*km

def overnight_costs(nights: int) -> float:
    """
    Bepaalt de overnachtingskosten op basis van het aantal nachten
    dat je op vakantie gaat.
    """
    return 60.0*nights

def total_costs(km: int, nights: int) -> int:
    """
    Bepaalt de totale kosten op basis van de afstand en het aantal
    nachten en rondt af naar hele euro's.
    Deze functie delegeert zoveel mogelijk werk naar de andere
    twee functies (roep die dus hier aan).
    """
    return roundmoney(travel_costs(km) + overnight_costs(nights))
    
def roundmoney(money: float) -> int:

if __name__ == '__main__':
    km = int(input('Hoe ver ga je weg in kilometers? '))
    nights = int(input('Hoe veel nachten is je verblijf? '))
    priceofvacation = total_costs(km, nights)
    print('Jouw vakantie kost:', priceofvacation)
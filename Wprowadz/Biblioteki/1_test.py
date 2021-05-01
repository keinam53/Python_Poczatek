import geopy


def run():
    adress = "Wolska 5/13 01-201 Warszawa"
    geolocator = geopy.Nominatim(user_agent="mieszkanie")
    adress_code = geolocator.geocode(adress)
    print(adress_code.latitude)
    print(adress_code.longitude)


if __name__ == '__main__':
    run()

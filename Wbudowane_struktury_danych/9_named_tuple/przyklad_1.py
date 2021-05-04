from collections import namedtuple

Location = namedtuple("Location", ["latitude", "longitude"])


def run():
    location = Location(54.23, 32.74)
    print(location.latitude)
    print(location.longitude)
    print(type(location))

    location_two = Location(latitude=59.32, longitude=41.02)
    print(location_two[0])

    for coord in location_two:
        print(coord)


if __name__ == '__main__':
    run()

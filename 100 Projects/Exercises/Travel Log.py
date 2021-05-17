travel_log = [
    {
        "Country": "France",
        "Visits": 12,
        "Cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "Country": "Germany",
        "Visits": 5,
        "Cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country['Country'] = country_visited
    new_country['Visits'] = times_visited
    new_country['Cities'] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

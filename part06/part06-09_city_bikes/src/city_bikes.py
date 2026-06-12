# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str):
    stations = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            stations.append(parts)

    station_data = {}
    for station in stations:
        station_data[station[3]] = (float(station[0]), float(station[1]))
    return station_data

def distance(stations: dict, station1: str, station2: str):
    import math
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    station_names = []
    for name in stations:
        station_names.append(name)
    
    greatest = 0
    stn1 = ""
    stn2 = ""
    for i in range(len(station_names)):
        for j in range(i+1, len(station_names)):
            station1 = station_names[i]
            station2 = station_names[j]
            distance_km = distance(stations, station1, station2)
            if distance_km > greatest:
                greatest = distance_km
                stn1 = station1
                stn2 = station2
    return stn1, stn2, greatest

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    print(stations)
    print()

    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    print()

    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    print()

    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
    
    





    


    






# In this exercise we will write some functions for working on a file containing location data from the stations 
# for city bikes in Helsinki.

# Each file will follow this format:

# Longitude;Latitude;FID;name;total_slot;operative;id
# 24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
# 24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
# 24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003
# Each station has a single line in the file. The line contains the coordinates, name, and other identifying 
# information for the station.

# Distance between stations
# First, write a function named get_station_data(filename: str). This function should read the names and locations 
# of all the stations in the file, and return them in a dictionary with the following format:

# Sample output
# {
#   "Kaivopuisto": (24.950292890004903, 60.155444793742276),
#   "Laivasillankatu": (24.956347471358754, 60.160959093887129),
#   "Kapteeninpuistikko": (24.944927399779715, 60.158189199971673)
# }
# Dictionary keys are the names of the stations, and the value attached is a tuple containing the location 
# coordinates of the station. The first element in the tuple is the Longitude field, and the second is the 
# Latitude field.

# Next, write a function named distance(stations: dict, station1: str, station2: str), which returns the distance 
# between the two stations given as arguments.

# The distance is calculated using the Pythagorean theorem. The multiplication factors below are approximate 
# values for converting latitudes and longitudes to distances in kilometres in the Helsinki region.

# # we will need the function sqrt from the math module 
# import math

# x_km = (longitude1 - longitude2) * 55.26
# y_km = (latitude1 - latitude2) * 111.2
# distance_km = math.sqrt(x_km**2 + y_km**2)
# Some examples of the function in action:

# stations = get_station_data('stations1.csv')
# d = distance(stations, "Designmuseo", "Hietalahdentori")
# print(d)
# d = distance(stations, "Viiskulma", "Kaivopuisto")
# print(d)
# Sample output
# 0.9032737292463177
# 0.7753594392019532


# The greatest distance
# Please write a function named greatest_distance(stations: dict), which works out the two stations on the list 
# with the greatest distance from each other. The function should return a tuple, where the first two elements 
# are the names of the two stations, and the third element is the distance between the two.

# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)
# Sample output
# Laivasillankatu Hietalahdentori 1.478708873076181


## Solution:

# data formate
# Longitude;Latitude;FID;name;total_slot;operative;id
# 24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
# 24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
# 24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003
# 24.941775800312996;60.16098589997938;4;Viiskulma;14;Yes;004
# 24.93628529982675;60.157948300373846;5;Sepankatu;32;Yes;005
def get_station_data(filename: str):
    with open(filename) as file_data:
        # file = file_data.read() ## for checking data formate
        # print(file)
        station_data = {}
        for data in file_data:
            data = data.replace("\n", "")
            data = data.split(";")
            if data[0] == 'Longitude':
                continue
            else :
                station_data[data[3]] = float(data[0]), float(data[1])
    return station_data

def distance(stations: dict, station1: str, station2: str):

    for key, value in stations.items():
        if key == station1:
            longitude1 = value[0]
            latitude1 = value[1]
        if key == station2:
            longitude2 = value[0]
            latitude2 = value[1]

    import math

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    station_names = []
    for key,value in stations.items():
        station_names.append(key)
    # print(station_names)

    station_1 = ''
    station_2 = ''
    max_distance = 0
    for station1 in station_names:
        for station2 in station_names:
            Distance = distance(stations, station1, station2)
            if Distance > max_distance:
                max_distance = Distance
                station_1 = station1
                station_2 = station2
    return station_1, station_2, max_distance


if __name__ == "__main__":
    # print(get_station_data('stations1.csv'))
    # stations = get_station_data('stations1.csv')
    # d = distance(stations, "Designmuseo", "Hietalahdentori")
    # print(d)
    # d = distance(stations, "Viiskulma", "Kaivopuisto")
    # print(d)

    stations = get_station_data('stations1.csv')
    # greatest_distance(stations)
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
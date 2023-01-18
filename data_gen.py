import random
import math
import datetime

station_list = [[500, 500], [500, -500], [-500, 500], [-500, -500]] #x[m], y[m]
target = [200, 300]
noise_value = 10  #[%]

speed_of_light = 299792458 #[m/s]

time_now = datetime.datetime.now()
print("Time zero: ", time_now.timestamp())

output = []

for station in station_list:
    print("Station: ", station, end="")

    distance = math.sqrt(math.pow(station[0]-target[0], 2) + math.pow(station[1]-target[1],2))
    print("\tdistance:", distance, end="")

    transmission_time = distance/speed_of_light
    noise = (transmission_time*((random.uniform(0, 1)*noise_value)/100))
    print(" \ttransmission_time: ", transmission_time*1000000, " \tnoise: ", noise*1000000, end="")

    arrival_time = time_now.timestamp() + transmission_time + noise

    output.append(arrival_time)
    print(" \tarrival_time: ", arrival_time)

print("input_data = ", output)

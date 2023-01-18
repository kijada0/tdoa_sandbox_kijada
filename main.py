import matplotlib.pyplot as plt
import math

# -------------------------------------------------------------------------------- #

station_list = [[500, 500], [500, -500], [-500, 500], [-500, -500]]
input_data = [1673990342.4827712, 1673990342.482773, 1673990342.4827724, 1673990342.4827738] #epoch timestamp

speed_of_light = 299792458 #[m/s]
curve_resolution = 100

# -------------------------------------------------------------------------------- #

def main():
    for i in range(len(station_list)):
        for j in range(i+1, len(station_list)):
            station_A = station_list[i]
            station_B = station_list[j]
            print("Station:", station_A, station_B)

            time_A = input_data[i]
            time_B = input_data[j]
            print("Times:", time_A, time_B)

            time_difference = time_A - time_B
            distance_difference = time_difference * speed_of_light
            station_distance = distance_between_points(station_A, station_B)
            print("Time diff: ", time_difference, " \tdistance diff: ", distance_difference, " \tstation dist:", station_distance)

            draw_curve(station_A, station_B, distance_difference)

            x = [station_A[0], station_B[0]]
            y = [station_A[1], station_B[1]]
            #plt.plot(x, y)

            print("")

    plt.grid()
    plt.show()


def distance_between_points(point_A, point_B):
    return math.sqrt(math.pow(point_A[0] - point_B[0], 2) + math.pow(point_A[1] - point_B[1], 2))


def draw_curve(station_1, station_2, distance_difference):
    points_x = []
    points_y = []

    # ---------- vertex assignment ----------
    if station_1[0] > station_2[0]:
        station_A = station_1
        station_B = station_2
    else:
        station_B = station_1
        station_A = station_2
        distance_difference *= -1

    station_distance = distance_between_points(station_A, station_B)

    for unknown_distance in range(curve_resolution):
        distance_AB = station_distance
        if distance_difference > 0:
            distance_AC = station_distance/2 + abs(distance_difference) + unknown_distance
            distance_BC = station_distance/2 - abs(distance_difference) + unknown_distance
        else:
            distance_AC = station_distance/2 - abs(distance_difference) + unknown_distance
            distance_BC = station_distance/2 + abs(distance_difference) + unknown_distance

        vertex_A, vertex_B = calculate_vertex(station_A, station_B, abs(distance_AC), abs(distance_BC), distance_AB)
        points_x.append(vertex_A[0])
        points_x.append(vertex_B[0])
        points_y.append(vertex_A[1])
        points_y.append(vertex_B[1])
        print("points:", points_x, points_y)

    plt.plot(points_x, points_y)


def calculate_vertex(point_A, point_B, distance_AC, distance_BC, distance_AB):
    vertex_Cpos = [0, 0]
    vertex_Cneg = [0, 0]

    print("Triangle rays:", distance_AC, distance_BC, distance_AB)

    # ---------- angle ----------
    bearing = get_bearing(point_A, point_B)
    print((math.pow(distance_BC, 2) + math.pow(distance_AB, 2) - math.pow(distance_AC, 2)) / (2 * distance_BC * distance_AB))
    alfa = math.acos((math.pow(distance_BC, 2) + math.pow(distance_AB, 2) - math.pow(distance_AC, 2)) / (2 * distance_BC * distance_AB))

    vertex_Cpos[0] = point_A[0] + math.cos((bearing + alfa)) * distance_AC
    vertex_Cpos[1] = point_A[1] + math.sin((bearing + alfa)) * distance_AC
    vertex_Cneg[0] = point_A[0] + math.cos((bearing - alfa)) * distance_AC
    vertex_Cneg[1] = point_A[1] + math.sin((bearing - alfa)) * distance_AC

    return vertex_Cpos, vertex_Cneg


def get_bearing(pointA, pointB):
    distance = distance_between_points(pointA, pointB)
    if pointA[1] < pointB[1]:
        alfa = math.pi - math.acos((pointA[0] - pointB[0]) / distance)
    else:
        alfa = 2*math.pi - math.acos((pointB[0] - pointA[0]) / distance)
    return alfa

main()
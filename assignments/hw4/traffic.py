"""
April Silva
traffic.py

Description: Completing homework 4.
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

def main():
    roads_surveyed = eval(input("How many roads were surveyed? "))
    total_days = 0
    total_vehicles = 0

    for i in range(roads_surveyed):
        vehicles_per_road = 0
        road_number = str(i + 1)
        user_input = eval(input("How many days was road " + road_number + " surveyed?"))
        for j in range(user_input):
            road_day = str(j + 1)
            input_values = eval(input("How many cars traveled on day " + road_day + "?"))
            vehicles_per_road = vehicles_per_road + input_values
        daily_average = vehicles_per_road / user_input
        print("Road " + road_number + " average vehicles per day: " + str(daily_average))
        total_vehicles = total_vehicles + vehicles_per_road
        total_days = total_days + user_input

    total_average_vehicles = total_vehicles / roads_surveyed
    print("Total number of vehicles traveled on all roads: " + str(total_vehicles))
    print("Average number of vehicles per road: " + str(total_average_vehicles))


if __name__ == '__main__':
    main()
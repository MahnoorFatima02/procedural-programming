# Question # 3: Calculate distance of two countries by their position of longitude and latitude

import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='flightgameuser',
    password='123Maa123',
    autocommit=True
)


def calculate_distance(airport_list):
    sql = "SELECT ID, ident, latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident = '" + airport_list[0] + "' OR ident = '" + airport_list[1] + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    query_result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in query_result:
            print(f"The airport latitude is {row[2]}. And it's longitude is {row[3]}. ")
    else:
        print("No found")

    distance = geodesic((query_result[0][2], query_result[0][3]),
                        (query_result[1][2], query_result[1][3])).km
    return distance


if __name__ == "__main__":
    airport_list = []
    for country in range(0, 2):
        airport_code = input("Enter your ICAO code here: ")
        airport_list.append(airport_code)

    print(f"DISTANCE : {round(calculate_distance(airport_list), 2)}")

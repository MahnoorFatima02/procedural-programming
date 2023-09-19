# Question # 2: airports types of country selected

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='flightgameuser',
    password='123Maa123',
    autocommit=True
)


def airport_location_order_type(country_name):
    sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country ='" + country_name + "'" + " GROUP BY type "
    cursor = connection.cursor()
    cursor.execute(sql)
    query_result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in query_result:
            print(f"There are {row[1]} {row[0]} in {country_name}. ")
    else:
        print("No found")

    return


if __name__ == "__main__":
    country_name_input = input("Enter your airport Area Code here: ")
    airport_location_order_type(country_name_input)

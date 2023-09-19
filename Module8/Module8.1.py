import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='flightgameuser',
    password='123Maa123',
    autocommit=True
)


def fetch_airport_location(ICAO_code):
    sql = "SELECT ID, ident,name, iso_country FROM airport"
    sql += " WHERE ident = '" + ICAO_code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    query_result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in query_result:
            print(f"The airport name is {row[2]}. It is located in {row[3]}. ")
    else:
        print("No found")
    return


if __name__ == "__main__":
    icao_number = input("Enter your ICAO Code here: ")
    fetch_airport_location(icao_number)

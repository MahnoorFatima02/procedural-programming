# Questions # 3: ICAO code and airport name
ICAO_and_airport_name = {'SASA': 'El Aybal Airport',
                         'YBOU': 'Boulia Airport', 'EFHK': 'Helsinki-Vantaa Airport'}


def enter_new_airport(ICAO_Code, airport_name):
    ICAO_and_airport_name[ICAO_Code] = airport_name
    print(ICAO_and_airport_name)


def fetch_airport_information(ICAO_Code_variable):
    print(ICAO_and_airport_name[ICAO_Code_variable])


print(" Hi, Good Day!!"
      " \n Do you want to: "
      "\n 1. Enter a new airport "
      "\n 2. Fetch the information of an existing airport "
      "\n 3. Quit")

input_selection = 0
while input_selection != 3:
    input_selection = int(input("Enter your option here: "))
    if input_selection == 1:
        ICAO_Code_input = input("Please enter the ICAO code of the airport: ")
        airport_name_input = input("name of the airport: ")
        enter_new_airport(ICAO_Code_input, airport_name_input)

    elif input_selection == 2:
        selected_ICAO_Code = input("Please enter the ICAO code of the airport here: ")
        fetch_airport_information(selected_ICAO_Code)

    else:
        print("You choose to quite!! BYE BYE")



# Question # 1: Enter a number to print out corresponding weather

seasons_tuple = ("Winter", "Spring", "Summer", "Autumn")
input_month_no = int(input("Please enter the number of month here: "))
winter_months = [1, 2, 12]
spring_months = [3, 4, 5]
summer_months = [6, 7, 8]
autumn_months = [9, 10, 11]

if input_month_no in winter_months:
    output_season = seasons_tuple[0]
    print(f"Your season as per your month selection is: ", output_season)

elif input_month_no in spring_months:
    output_season = seasons_tuple[1]
    print(f"Your season as per your month selection is: ", output_season)

elif input_month_no in summer_months:
    output_season = seasons_tuple[2]
    print(f"Your season as per your month selection is: ", output_season)

elif input_month_no in autumn_months:
    output_season = seasons_tuple[3]
    print(f"Your season as per your month selection is: ", output_season)

else:
    print("Oops!! Invalid number")

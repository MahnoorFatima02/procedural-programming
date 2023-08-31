# Question 1: length of zander

zander_length = input("Please enter your zander length in cm here: ")
standard_zander_length = 42
if int(zander_length) < standard_zander_length:
    print("The zander length is less than standard requirement, please release the fish back in the lake.")
    gap_in_length = standard_zander_length - int(zander_length)
    print("Your caught fish was " + str(gap_in_length) + " cm below the size limit.")
else:
    print("Good!! You have caught the right size fish!")

# Question 2: cabin class
cabin_class = input("Please enter your cabin class below: ")
cabin_class_LUX = "LUX"
cabin_class_A = "A"
cabin_class_B = "B"
cabin_class_C = "C"
if cabin_class.upper() == cabin_class_LUX:
    print("upper-deck cabin with a balcony")
elif cabin_class.upper() == cabin_class_A:
    print("above the car deck, equipped with a window")
elif cabin_class.upper() == cabin_class_B:
    print("windowless cabin above the car deck")
elif cabin_class.upper() == cabin_class_C:
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class, please choose a correct class and try again!")


# Question 3: biological gender and hemoglobin value (g/l)

gender_identity = input("Please enter your gender in F/M: ")
hemoglobin_value = input("Please enter your hemoglobin value in g/l: ")
male = "M"
female = "F"
male_high_hemoglobin = 167
male_low_hemoglobin = 134
female_high_hemoglobin = 155
female_low_hemoglobin = 117

if gender_identity == female:
    if int(hemoglobin_value) > female_high_hemoglobin:
        print("Your hemoglobin level is high")
    elif int(hemoglobin_value) < female_low_hemoglobin:
        print("Your hemoglobin level is low")
    else:
        print("Your hemoglobin level is normal")
elif gender_identity == male:
    if int(hemoglobin_value) > male_high_hemoglobin:
        print("Your hemoglobin level is high")
    elif int(hemoglobin_value) < male_low_hemoglobin:
        print("Your hemoglobin level is low")
    else:
        print("Your hemoglobin level is normal")
else:
    print("Gender not defined")

# Question 4: leap year

input_year = input("Please enter your year here: ")

if int(input_year) % 4 == 0 and int(input_year) % 100 != 0:
    print("This is a leap year")
elif int(input_year) % 4 == 0 and int(input_year) % 400 == 0:
    print("The year is a leap year")
else:
    print("This is not a leap year")












# Questions # 2

existing_set = set()
add_name = "test"


def name_to_add(name_value):
    if name_value in existing_set:
        print("This name already exists !! Try a new one again")
    else:
        print("It's a new name !")
        existing_set.add(name_value)
    return


while add_name != "":
    add_name = input("Enter the name you want to add here: ")
    if add_name != "":
        name_to_add(add_name)

for name in existing_set:
    print(name)

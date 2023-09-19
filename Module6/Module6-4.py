# Question # 4: sum of list of integers

def sum_of_list(numbers):
    sum_of_numbers = 0
    for i in numbers:
        sum_of_numbers = sum_of_numbers + i
    return sum_of_numbers


if __name__ == "__main__":
    integer_list = []
    max_number_of_input = 6
    while len(integer_list) < max_number_of_input:
        integer_value = int(input("Please enter integer to add into list: "))
        integer_list.append(integer_value)

    sum_of_integers = sum_of_list(integer_list)
    print("The sum of list of integers is ", sum_of_integers)

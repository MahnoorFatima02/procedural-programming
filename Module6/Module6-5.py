# Question # 5: extract even values from list

def get_even_values(numbers):
    even_result = []
    for number in numbers:
        if number % 2 == 0:
            even_result.append(number)
    return even_result


if __name__ == "__main__":
    original_list = []
    maximum_length_list = 7
    while len(original_list) < maximum_length_list:
        value_required = int(input("Enter value you want to add into list here: "))
        original_list.append(value_required)

    even_list = get_even_values(original_list)

    print(f"Your original list was:  {original_list}")
    print(f"Your modified even list is:  {even_list}")

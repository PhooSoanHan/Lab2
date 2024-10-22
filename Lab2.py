def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    temp = input()
    x = temp.split()
    temp_list = [float(temp) for temp in x]
    print (temp_list)
    return temp_list

def calc_average_temperature(temp_list):
    y = sum(temp_list)
    avg = y / len(temp_list)
    print(float(avg))
    return avg

def calc_min_max_temperature(temp_list):
    mintemp = min(temp_list)
    maxtemp = max(temp_list)
    min_max_list = [mintemp, maxtemp]
    print ( min_max_list)
    return min_max_list

def sort_temperature(temp_list):
    temp_list.sort()
    print (temp_list)
    return temp_list

def calc_median_temperature(temp_list):
    temp_list.sort()
    if len(temp_list) % 2 == 0:
        median = (temp_list[len(temp_list) // 2 - 1] + temp_list[len(temp_list) // 2]) / 2
    else:
        median = temp_list[len(temp_list) // 2]
    print (median)
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    temp_list = get_user_input()
    calc_average_temperature(temp_list)
    calc_min_max_temperature(temp_list)
    sort_temperature(temp_list)
    calc_median_temperature(temp_list)

if __name__ == "__main__":
    main()
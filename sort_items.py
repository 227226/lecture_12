import csv
import os
import random

cwd_path = os.getcwd()


def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as numbers_file:
        reader = csv.reader(numbers_file, delimiter="\t")
        for row in reader:
            number_row = []
            for element in row:
                element = int(element)
                number_row.append(element)
    return number_row


def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as numbers_file:
        reader = csv.reader(numbers_file, delimiter=",")
        row_list = []
        for row in reader:
            row_list.append(row)

    row = row_list[row_number]
    number_row = []
    for element in row:
        element = int(element)
        number_row.append(element)
    return number_row



def selection_sort(number_array, direction="ascending"):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """
    for i in range(len(number_array)):
        min_idx = i
        for num_i in range(i + 1, len(number_array)):
            if direction == "ascending":
                if number_array[min_idx] > number_array[num_i]:
                    min_idx = num_i
            elif direction == "descending":
                if number_array[min_idx] < number_array[num_i]:
                    min_idx = num_i
        number_array[i], number_array[min_idx] = number_array[min_idx], number_array[i]
    return number_array


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """
    for index in range(len(number_array) - 1):
        for i in range(0, len(number_array) - index - 1):
            if number_array[i] > number_array[i + 1]:
                number_array[i], number_array[i + 1] = number_array[i + 1], number_array[i]
    return number_array


def main():
    row = read_row("numbers_one.csv")
    print(row)

    # Ukol: Selection Sort
    number_array = selection_sort(row)
    print(number_array)


    # Ukol: Selection Sort - se smerem razeni
    number_array = selection_sort(row, direction="descending")
    print(number_array)

    # Ukol: Bubble Sort
    row_number = random.randint(0, 2)
    row = read_rows("numbers_two.csv", row_number)
    print(row)
    sorted_row = bubble_sort(row)
    print(sorted_row)

    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()


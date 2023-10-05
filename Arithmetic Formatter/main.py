from itertools import count
import re


def arithmetic_arranger(list1):
    arithmetic_arranger1 = list1
    if len(list1) > 5:
        print('Error: Too many problems.')
        exit()

    arr = []
    main_arr = []

    i = 0

    # we will use this function to lone an array and add it into main array
    # such that it will be in form of list within list
    def cloning(arr):
        li_copy = arr[:]
        return li_copy

    # checking whether the entered data consists of alphabets
    def only_digits():
        value = problem
        all_value = re.findall(r'[0-9]+', value)
        only_alphabets = re.findall(r'[a-z.A-Z]+', value)
        if len(only_alphabets) != 0:
            print("Error: Numbers must only contain digits")
        else:
            if split_arithmetic_arranger[1] == '+':
                # sum operation
                operation = int(split_arithmetic_arranger[0]) + int(split_arithmetic_arranger[2])
            elif split_arithmetic_arranger[1] == '-':
                # difference operation
                operation = int(split_arithmetic_arranger[0]) - int(split_arithmetic_arranger[2])

            count_1 = int(len(split_arithmetic_arranger[0]))
            count_3 = int(len(split_arithmetic_arranger[2]))

            show_elements(count_1, count_3, operation)

    # to print arithmetic operations vertically and perform sum and difference operation
    def show_elements(count_1, count_3, operation):
        if count_1 > 4 or count_3 > 4:
            print('Error: Numbers cannot be more than four digits.')
            exit()

        elif count_1 == count_3 or count_1 < count_3:
            second_row = 2 + count_3

            first_row = second_row - count_1

            first = (' ' * first_row) + split_arithmetic_arranger[0]
            second = split_arithmetic_arranger[1] + ' ' + split_arithmetic_arranger[2]
            third = '_' * second_row

            # for spacing of the answer
            third_row = second_row - len(str(operation))
            fourth = ' ' * third_row + str(operation)

            arr.append(first)
            arr.append(second)
            arr.append(third)
            arr.append(fourth)


        else:
            first_row = 2 + count_1
            second_row = first_row - (count_3 + 1)


            first = ' ' * 2 + split_arithmetic_arranger[0]
            second = split_arithmetic_arranger[1] + ' ' * second_row + split_arithmetic_arranger[2]
            third = '_' * first_row

            # for spacing of the answer
            third_row = first_row - len(str(operation))
            fourth = ' ' * third_row + str(operation)

            arr.append(first)
            arr.append(second)
            arr.append(third)
            arr.append(fourth)

        copied_list = cloning(arr)
        main_arr.append(copied_list)
        arr.clear()



    for problem in arithmetic_arranger1:
        split_arithmetic_arranger = arithmetic_arranger1[i].split()

        if split_arithmetic_arranger[1] == '+':
            only_digits()
            i += 1

        if split_arithmetic_arranger[1] == '-':
            only_digits()
            i += 1

        if split_arithmetic_arranger[1] != '-' and split_arithmetic_arranger[1] != '+':
            print('Error: Operator must be "+" or "-" .')
            i += 1


    # print(main_arr)
    # to print problems side by side
    for i in main_arr:
        print(" " * 4, i[0], end="")
    print("  ")
    for i in main_arr:
        print(" " * 4, i[1], end="")
    print("  ")
    for i in main_arr:
        print(" " * 4, i[2], end="")
    print("  ")
    for i in main_arr:
        print(" " * 4, i[3], end="")


arithmetic_arranger(["1111 + 1911", "123 + 1", "234 * 1232", "234 - 1232", "QWE - 432"])

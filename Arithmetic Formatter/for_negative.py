# for + operator

arithmetic_arranger = ["32 - 8", "1 - 3801", "9999 - 9999", "523 - 49"]


i = 0
for problem in arithmetic_arranger:

    split_arithmetic_arranger = arithmetic_arranger[i].split()


    difference_ar = int(split_arithmetic_arranger[0]) - int(split_arithmetic_arranger[2])

    count_1 = int(len(split_arithmetic_arranger[0]))
    count_3 = int(len(split_arithmetic_arranger[2]))

    if count_1 > 4 or count_3 > 4:
        print('Error: Numbers cannot be more than four digits.')
        exit()

    elif count_1 == count_3 or count_1 < count_3:
        second_row = 2 + count_3

        first_row = second_row - count_1


        print((' ' * first_row) + split_arithmetic_arranger[0])
        print(split_arithmetic_arranger[1] + ' ' + split_arithmetic_arranger[2])
        print('_' * second_row)

        # for spacing of the answer
        third_row = second_row - len(str(difference_ar))
        print(' ' * third_row + str(difference_ar))

        i += 1

    else:
        first_row = 2 + count_1
        second_row = first_row - (count_3 + 1)

        print((' ' * 2 + split_arithmetic_arranger[0]))
        print(split_arithmetic_arranger[1] + ' ' * second_row + split_arithmetic_arranger[2])
        print('_' * first_row)

        # for spacing of the answer
        third_row = first_row - len(str(difference_ar))
        print(' ' * third_row + str(difference_ar))

        i += 1

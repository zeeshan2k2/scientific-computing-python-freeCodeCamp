# for + operator

arithmetic_arranger = ["1111 + 1911"]


split_arithmetic_arranger = arithmetic_arranger[0].split()

sum_ar = int(split_arithmetic_arranger[0]) + int(split_arithmetic_arranger[2])

count_1 = int(len(split_arithmetic_arranger[0]))
count_3 = int(len(split_arithmetic_arranger[2]))

if count_1 > 4 or count_3 > 4:
    print('Error: Numbers cannot be more than four digits.')
    exit()

elif count_1 == count_3 or count_1 < count_3:
    second_row = 2 + count_3
    print(second_row)

    first_row = second_row - count_1
    print(first_row)


    firstr = ' ' * first_row + split_arithmetic_arranger[0]
    secondr = split_arithmetic_arranger[1] + ' ' + split_arithmetic_arranger[2]
    thirdr = '_' * second_row

    # for spacing of the answer
    third_row = second_row - len(str(sum_ar))
    fourthr = ' ' * third_row + str(sum_ar)

    print(firstr , "\n", secondr, "\n", thirdr, "\n", fourthr, end='')


else:
    first_row = 2 + count_1
    second_row = first_row - (count_3 + 1)

    firstr = (' ' * 2 + split_arithmetic_arranger[0])
    secondr = (split_arithmetic_arranger[1] + ' ' * second_row + split_arithmetic_arranger[2])
    thirdr = ('_' * first_row)

    # for spacing of the answer
    third_row = first_row - len(str(sum_ar))
    fourthr = (' ' * third_row + str(sum_ar))
    print((firstr, "\n", secondr, "\n", thirdr, "\n", fourthr), end='')





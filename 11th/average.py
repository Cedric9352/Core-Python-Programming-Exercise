from operator import add


def average(*nkargs):

    arg_list = []
    for eachArgs in nkargs:
        arg_list.append(eachArgs)
    sum_ave = reduce(add, arg_list)
    ave = float(sum_ave) / len(arg_list)

    return ave

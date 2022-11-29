
def cleaner21(csv, key_names, kind=0, filename=None):
    with open(csv) as f:
        line_list = []  # q list to carry all the separated lines
        for line in f:
            line2 = line.split(',')
            line2[5] = line2[5].replace('\n', '')
            line_list.append(line2)

    """ the creation of a dictionarty that has keys from a list """
    dic_mini = {}  # a dictionary that has keys from a list provided
    dic_minini = {}  # used for the creation of a dictionary with the keys from a list

    for key in key_names:
        dic_minini[key] = ''
        dic_mini.update(dic_minini)

    print(dic_mini)

    """ the creation of a list that contains a dictionary with values of a csv file
        it will loop through the list and assign the values to the keys in the dictionary
        a new dictionary,called dic_sub, will be created for the assignment and appendage to dict_list
     """
    dict_list = []  # a list that contains all the dictionaries
    for line in line_list:
        i = 0
        dic_sub = {}  # will have the same keys as the dic_mini but for re-assignment purposes
        dict_list.append(dic_sub)
        for key in dic_mini.keys():
            try:
                dic_sub[key] = line[i]  # to reassign the keys from the list to the values from the csv file
                i += 1
            except IndexError:  # to keep the indexing in the range of the lines elements
                break

    if kind == 1:
        if filename is None:
            filename = csv.replace('.', ' listed-dictionary.')
            g = open(filename, 'w')
        else:
            g = open(filename, 'w')

        g.write(str(dict_list))
        return dict_list

    elif kind == 0:
        return dict_list, dic_mini

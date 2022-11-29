

def cleaner2(csv, filename=None, kind=0):

    with open('csv') as f:
        # string = f.read()
        line_list = []
        for line in f:
            line2 = line.split(',')
            line2[5] = line2[5].replace('\n', '')
            line_list.append(line2)
            # line2[5] = line2[5].replace('\n', '')

    # print(line_list)
    dict_list = []
    for lists in line_list:
        dic = {'name': lists[0], 'sport': lists[1], 'nation': lists[2], 'age': lists[3], 'wt': lists[4], 'ht': lists[5]}
        dict_list.append(dic)

    if kind == 1:
        if filename is None:
            filename = csv.replace('.', ' listed-dictionary.')
            g = open(filename, 'w')
        else:
            g = open(filename, 'w')

        g.write(str(dict_list))
        return dict_list

    elif kind == 0:
        return dict_list

def dictionize(csv, filename=None, type=1):
    if type == 1:
        if filename is None:
            filename = csv.replace('.', ' dictionary.')
            g = open(filename, 'w')
        else:
            g = open(filename, 'w')

        g = open(filename, 'a')
        g.write('{\n')
        with open(csv) as f:
            dicts = {}
            for line in f:
                line2 = line.split(',')
                line2[5] = line2[5].replace('\n', '')
                dicts.update({line2[0]: line2})

                g.write(f"'{line2[0]}': {line2}, \n")

        g.write('}')
        # g.close()
        return dicts

    if type == 0:
        with open(csv) as f:
            dicts = {}
            for line in f:
                line2 = line.split(',')
                line2[5] = line2[5].replace('\n', '')
                dicts.update({line2[0]: line2})


# "I:\\Programmer's pack\\Files and Docs\\CSV files\\Sample data - Athletes.csv")

dic = dictionize('snip csv.txt', 0)
print(dic.values())

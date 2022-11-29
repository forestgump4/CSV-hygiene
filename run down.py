# import re
#
# #
# #
# # dic = {'Name': ['Name', 'Sport', 'Nationality', 'Age', 'Wt kg', 'Ht'],
# # 'ABBAS Muhammad': ['ABBAS Muhammad', 'Alpine Skiing', 'Pakistan', '23', '55', '168'],
# # 'ABBOTT Jeremy': ['ABBOTT Jeremy', 'Figure Skating', 'United States', '24', '', '175'],
# # 'ABLAEV Enver': ['ABLAEV Enver', 'Freestyle Skiing', 'Ukraine', '30', '68', '169'],
# # 'ABRAMASHVILI Iason': ['ABRAMASHVILI Iason', 'Alpine Skiing', 'Georgia', '21', '82', '176'],
# # 'ABRAMENKO Evgeny': ['ABRAMENKO Evgeny', 'Biathlon', 'Belarus', '22', '81', '180'],
# # 'ABRAMENKO Oleksandr': ['ABRAMENKO Oleksandr', 'Freestyle Skiing', 'Ukraine', '21', '74', '179'],
# # 'ABRAMOVA Yekaterina': ['ABRAMOVA Yekaterina', 'Speed Skating', 'Russia', '27', '65', '167'],
# # 'ABRAMOVITCH Dmitry': ['ABRAMOVITCH Dmitry', 'Bobsleigh', 'Russia', '27', '96', '182'],
# # 'ACHI Ghassan': ['ACHI Ghassan', 'Alpine Skiing', 'Lebanon', '16', '60', '168'],
# # 'ACTON Brigitte': ['ACTON Brigitte', 'Alpine Skiing', 'Canada', '24', '63', '167'],
# # 'ADJEI Richard': ['ADJEI Richard', 'Bobsleigh', 'Germany', '27', '110', '190'],
# # 'AEBLI Christian': ['AEBLI Christian', 'Bobsleigh', 'Switzerland', '31', '97', '180'],
# # 'AFINOGENOV Maxim': ['AFINOGENOV Maxim', 'Ice Hockey', 'Russia', '30', '88', '183'],
# # 'AGOSTA Meghan': ['AGOSTA Meghan', 'Ice Hockey', 'Canada', '23', '66', '168'],
# # 'AGOSTO Benjamin': ['AGOSTO Benjamin', 'Figure Skating', 'United States', '28', '', '178'],
# # }
# # #
# # # dictionary = {}
# # # with open("snip csv dictionary.txt") as file:
# # #     for line in file:
# # #         (key, value) = line.split(': ')
# # #
# # #         dictionary[key] = value
# # # print(repr(dictionary))
# #
# # with open('snip csv dictionary.txt', 'r') as f:
# #     aall = f.read()
# #     dict(aall)
# #     print(repr(aall))
# #
# # # for i in range(1, len(all)):
# # #     print(aall[2*i])
# # # for key in aall:
# # #     list = dic[key]
# # #     print(list)
# # #     # for elements in list:
# # #     #
#
#
# with open('snip csv dictionary.txt') as f:
#     file = f.read()
#     a = eval(re.search(r"\{(.*?)\}", file).group(0))
#     print(kind(a))
#
# # print(list(file))
# # print(repr(file))
# # print(repr(file[0]))
# # print(kind(file[0]))
#
#
# # import re
# # import ast
# # x = ast.literal_eval(re.search('({.+})', file).group(0))
# # print(kind(x))
#
#
#
#
# # data = "Some string created {'Foo': u'1002803', 'Bar': 'value'} string continue etc."
#
# a = eval(re.search(r"\{(.*?)\}", file).group(0))
# print(kind(a))

def dictionize(csv, kind=1, filename=None):
    if kind == 1:
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
        g.close()
        return dicts

    if kind == 0:
        with open(csv) as f:
            dicts = {}
            for line in f:
                line2 = line.split(',')
                line2[5] = line2[5].replace('\n', '')
                dicts.update({line2[0]: line2})

        return dicts


dictionary = dictionize('snip csv.txt', 0)
final = {'Name': '', 'Sport':'', 'Nationality': '', 'Age': '', 'Wt kg': '', 'Ht': ''}
# for value in dictionary.values():
#     for key in final.keys():
#         for element in value:
#             final[key] = element
#             # break
# print(final)

a = list(final.keys())
b = list(dictionary.values())
print(type(a), type(b))

j = 0
i = 0

while j in range(len(b)) and i in range(6):
    final[a[i]] = b[j][i]
    print(final)
    print(i,   j)
    j += 1
    i += 1
    if i == 6:
        i = 0

import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def info():
    pattern = r'(\+7|8)[-\s*]?\(?(\d{3})\)?[-\s*]?(\d+)[-\s*]?(\d{2})[-\s*]?(\d{2})\s?((\()?(\w+)(\.)(\s)(\d+)(\))?)?'
    sub = r'+7(\2)\3-\4-\5 \8\9\10\11'
    temple_list = []
    for el in contacts_list:
        full_name = ' '.join(el[:3]).split(' ')
        surname = full_name[0]
        name = full_name[1]
        lastname = full_name[2]
        number = re.sub(pattern, sub, el[5])
        email = el[6]
        temple_list.append([surname, name, lastname, number, email])
    return temple_list


def union(temple_list):
    dict_1 = {}
    dict_2 = {}
    for i, word1 in enumerate(temple_list):
        dict_1[word1[0], word1[1]] = [word1[2], word1[3], word1[4]]
        for word2 in temple_list[i + 1:]:
            if word1[0] == word2[0]:
                for el in word2:
                    if el not in word1:
                        word1.append(el)
                        word1.remove('')
                    dict_2[word1[0], word1[1]] = [word1[2], word1[3], word1[4]]
    new_dict = dict(list(dict_1.items()) + list(dict_2.items()))
    new_list = []
    for k, v in list(new_dict.items()):
        res = list(k)+list(v)
        new_list.append(res)
    return new_list


with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(union(info()))

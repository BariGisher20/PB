import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def info():
    pattern = r'(\+7|8)[-\s*]?\(?(\d{3})\)?[-\s*]?(\d+)[-\s*]?(\d{2})[-\s*]?(\d{2})\s?((\()?(\w+)(\.)(\s)(\d+)(\))?)?'
    sub = r'+7(\2)\3-\4-\5 \8\9\10\11'
    temple_list = []
    set_l = dict()
    for el in contacts_list:
        full_name = ' '.join(el[:3]).split(' ')
        surname = full_name[0]
        name = full_name[1]
        lastname = full_name[2]
        number = re.sub(pattern, sub, el[5])
        email = el[6]
        temple_list.append([surname, name, lastname, number, email])
    return temple_list


def union(list):
    new_list = []
    for i, word1 in enumerate(list):
        for word2 in list[i + 1:]:
            for el in word1:
                if el not in word2:
                    if word1[0] == word2[0]:
                        word2.append(el)
                        new_list.append(word2)
                    else:
                        new_list.append(word1)
    return new_list


with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(union(info()))









#
# def union():
#     set_l = dict()
#     for i in res:
#         set_l[surname, name] = number, email
#         pprint(set_l)


    # surname_list = []
    # name_list = []
    # for surname in res:
    #     if surname not in surname_list:
    #         surname_list.append(surname)
    # name_list.append(name)
    #     set_l = dict(zip(surname_list, name_list))
        # pprint(set_l)
    # pprint(fio)
        # surname_list = []
        # name_list = []
        # for elem in fio:
        #     surname_cp = elem[0]
        #     if surname_cp not in surname_list:
        #         surname_list.append(surname_cp)
    #         res_2 = [surname_list, name, lastname, number, email]
    #         fio.append(res_2)
    #
    # pprint(fio)
    # pprint(surname_list)

        # if surname not in surname_list:
        #     surname_list.append(surname)

    # for element in fio:
    #     if element[0] not in surname_list:
    #         surname_list.append(element[0])
    #     name_list.append(element[1])
    #     set_l = dict(zip(surname_list, name_list))
    #     for k in set_l:
    #         res_2 = [k, element[1], element[2], element[3], element[4]]
    #         fio.append(res_2)
    # pprint(fio)












# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)


if __name__ == '__main__':
    pprint(main())


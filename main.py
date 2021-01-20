import html_parse
import csv
import numpy
import itertools

INPUT_CSV = "chouseisan.csv"
OUTPUT_CSV = "mail_list.csv"

def trim(string):
    spaces = " 　"
    for space in spaces:
        string = string.replace(space,"")
    return string

def search_mail_address(name):
    list = [data[2] for data in html_parse.mail_list if trim(name) and name in trim(data[1])]
    return list

with open(INPUT_CSV,mode="r",encoding="s-jis") as ip:
    csv_data = list(csv.reader(ip))

    title = csv_data[0][0]
    member_list = [trim(name) for name in csv_data[2][1:]]

    schedule_data = []
    for data in csv_data[3:]:
        if data[0] != "コメント" :
            schedule_data.append({
                data[0]:
                [x*y for x,y in zip(member_list,[state != "×" for state in data[1:]])]
            })

with open(OUTPUT_CSV,mode="w",encoding="s-jis") as op:
    writer = csv.writer(op)

    for data in schedule_data:
        writer.writerow(data.keys())
        member_mail_list = []
        for name in list(data.values())[0]:
            print(name)
            member_mail_list.append(search_mail_address(name))
        writer.writerow(itertools.chain.from_iterable(member_mail_list))

print("end")
from html.parser import HTMLParser
import re

SRC_FILE = "mail_sample.html"

class MailTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.table_flg = False
        self.tr_flg = False
        self.td_flg = False
        self.td_data = []
        self.table_data = []

    def handle_starttag(self, tag, attrs):
        if re.match("^table$", tag):
            self.table_flg = True

        if re.match("^tr$", tag):
            self.tr_flg = True

        if re.match("^td$", tag):
            self.td_flg = True


    def handle_endtag(self, tag):
        if re.match("^table$", tag):
            self.table_flg = False

        if re.match("^tr$", tag):
            self.tr_flg = False

        if re.match("^td$", tag):
            self.td_flg = False


    def handle_data(self, data):
        if self.table_flg and self.tr_flg and self.td_flg:
            self.td_data.append(data)

        elif self.table_flg and not self.tr_flg:
            self.table_data.append(self.td_data.copy())
            self.td_data = []


parser = MailTableParser()
with open(SRC_FILE,mode="r",encoding="utf-8") as ip:
    target = "".join(ip.readlines())
    parser.feed(target)

mail_list = []
if len(parser.table_data) > 0:
    for data in parser.table_data:
        if len(data) >= 3:
            # mail_list.append([data[0],data[1].split(" "),data[2]])
            mail_list.append([data[0],data[1],data[2]])
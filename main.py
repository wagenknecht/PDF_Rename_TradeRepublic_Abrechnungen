import datetime

import fitz
from os import DirEntry, curdir, getcwd, chdir, rename
from glob import glob as glob

directory = 'PDF_FILES'
chdir(directory)

pdf_list = glob('*.pdf')

for pdf in pdf_list:
    with fitz.open(pdf) as pdf_obj:
        text = pdf_obj[0].get_text()
        information = list(text.split("\n"))
        for string in information:
            if string.startswith("Market-Order"):
                details = string
                break
        details = details.split(' ')

        # date operations
        transaction_date = datetime.datetime.strptime(details[3], "%d.%m.%Y,")
        for i in information:
            print(i)
        print(details[5])
        transaction_time = datetime.datetime.strptime(details[5], "%H:%M")
        transaction_isodate = datetime.datetime.combine(transaction_date.date(), transaction_time.time())

        # welche Aktie / ETF
        for index, string in enumerate(information):
            if string.startswith("BETRAG"):
                index_aktie = index + 1
                break

        new_file_name = str(transaction_isodate).replace(":", "-") + ' ' + details[1] + ' ' + information[index_aktie].replace(".", "")
        print(new_file_name)
    rename(pdf, new_file_name + '.pdf')

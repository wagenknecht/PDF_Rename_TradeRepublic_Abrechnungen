import datetime

import fitz
from os import DirEntry, curdir, getcwd, chdir, rename
from glob import glob as glob

directory = 'Abrechnungen'
chdir(directory)

pdf_list = glob('*.pdf')

for pdf in pdf_list:
    with fitz.open(pdf) as pdf_obj:
        text = pdf_obj[0].get_text()
        information = list(text.split("\n"))
        details = information[32].split(' ')

        # date operations
        transaction_date = datetime.datetime.strptime(information[11], "%d.%m.%Y")
        transaction_time = datetime.datetime.strptime(details[5], "%H:%M")
        transaction_isodate = datetime.datetime.combine(transaction_date.date(), transaction_time.time())

        new_file_name = str(transaction_isodate).replace(":", "-") + ' ' + details[1] + ' ' + information[38].replace(".", "")
    rename(pdf, new_file_name + '.pdf')

import os, platform, csv

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

my_file = "#38 - MOUREDEVPRO CSV/newsletter_users.csv"



def read_list_csv():
    with open(my_file) as file:
        content_list_csv = csv.reader(file, delimiter=';')
        next(content_list_csv)
        for row in content_list_csv:
            print('El email es:', row[1])
read_list_csv()
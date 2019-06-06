# import locale
#
# def_text_coding = locale.getpreferredencoding()
# print(def_text_coding)

"""
import csv

with open('data.csv', encoding='utf-8') as file:
    file_reader = csv.reader(file)
    for row in file_reader:
        print(row)

new_data = ['Lynnfield', 'LGA1156', 'Интел', 'i5-750S', 4, 4, 2.66]

with open('data.csv', 'a', encoding='utf-8', newline='') as file:
    file_writer = csv.writer(file)
    file_writer.writerow(new_data)
"""

########################################################################################

"""
import json

with open('data.json', encoding='utf-8') as file:
    json_obj = json.load(file)
    print(json_obj)
    print(type(json_obj))


# with open('data.json', encoding='utf-8') as file:
#     json_content = file.read()
#     json_obj = json.loads(json_content)
#     print(json_obj)
#     print(json_obj['message'])

with open('data.json', 'w', encoding='utf-8') as file:
    json_obj['ip_address'] = 'ip_адрес'
    json.dump(json_obj, file, sort_keys=True, indent=2)
"""

########################################################################################

import yaml

with open('data.yaml', encoding='utf-8') as file:
    file_content = yaml.load(file, Loader=yaml.SafeLoader)
    print(file_content)

with open('data.yaml', 'a', encoding='utf-8') as file:
    new_data_to_yaml = [{'action': 'msg_3', 'encoding': 'ascii', 'from': 'account_name_3'}]
    yaml.dump(new_data_to_yaml, file, default_flow_style=False)

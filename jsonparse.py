import json

# courses = '{"name": "Emmanuel", "languages": ["Java", "Python"]}'
#
# #loads methos parse json string and it returns dictionary
# dict_courses = json.loads(courses)
# print(type(dict_courses))
# print(dict_courses)
# print(dict_courses['languages'][0:2])

# container = dict_courses['languages']
# print(container[0])

# parse content present in json files

with open('C:\\Users\\EMMYTECH\\PycharmProjects\\JSON\\file.json') as f:
    data = json.load(f)
    # print(data)
    # print(data["topping"][1]['type'])
    for value in data['topping']:
        if value['type'] == "Glazed":
            print((value['age']))
            assert value['age']== 29

# TO COMPARE 2 JSON FILES
with open('C:\\Users\\EMMYTECH\\PycharmProjects\\JSON\\second_json.json') as f1:
    data2 = json.load(f1)
    assert data == data2